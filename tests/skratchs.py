import numpy as np
import cv2 as cv

from multiprocessing.pool import ThreadPool
from collections import deque

import dbr
from dbr import *

BarcodeReader.init_license("t0068lQAAAJo4Zphb/H5u+hXkMvNYkvJaugGDuxhkxlHomBIS5p+ik4EniQHb+nJT0Etw4jT62Tk0eDNSocYKOJBwBRQjoxY=;t0068lQAAAJk9a1kS3kziyId8qSP5UVnwj3EaWWBtK+Tb+z8pfy0vmn+7H2DaXfKRWaqe5SGIQNwplT7CnjzGG7RCimgStO0=")

reader = BarcodeReader()


threadn = 1 # cv.getNumberOfCPUs()
pool = ThreadPool(processes = threadn)
barcodeTasks = deque()

def process_frame(frame):
    results = None
    try:
        results = reader.decode_buffer(frame)
    except BarcodeReaderError as bre:
        print(bre)
    
    return results

cap = cv.VideoCapture(2)
i = 0
while True:
    ret, frame = cap.read()
    while len(barcodeTasks) > 0 and barcodeTasks[0].ready():
        results = barcodeTasks.popleft().get()
        if results != None:
            for result in results:
                points = result.localization_result.localization_points
                # cv.line(frame, points[0], points[1], (0,255,0), 2)
                # cv.line(frame, points[1], points[2], (0,255,0), 2)
                # cv.line(frame, points[2], points[3], (0,255,0), 2)
                # cv.line(frame, points[3], points[0], (0,255,0), 2)
                # cv.putText(frame, result.barcode_text, points[0], cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
                print(result.barcode_text, i)
                i += 1


    if len(barcodeTasks) < threadn:
        task = pool.apply_async(process_frame, (frame.copy(), ))
        barcodeTasks.append(task)

    cv.imshow('Barcode & QR Code Scanner', frame)
    ch = cv.waitKey(1)
    if ch == 27:
        break
    