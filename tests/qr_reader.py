#!/user/bin/env python3

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
import time
 
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
url='http://192.168.174.109/'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
 
prev=""
pres=""
while True:
    time.sleep(0.1)
    img_resp=urllib.request.urlopen(url+'640x480.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
 
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres=obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            print("Data: ",obj.data)
            prev=pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 255, 0), 3)
 
    cv2.imshow("live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cv2.destroyAllWindows()