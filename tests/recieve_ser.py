#!/user/bin/env python3

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(2.)
ser.reset_input_buffer()

print("Serial initilized")

try:
    while True:
        time.sleep(0.01)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print('close serial')
    ser.close()
