#!/user/bin/env python3

import serial
import time, random

ser = serial.Serial('/dev/ttyUSB3', 115200, timeout=1.0)
time.sleep(2.)
ser.reset_input_buffer()

print("Serial initilized")

try:
    while True:
        ser.write(f"vs: 001-001\n".encode('utf-8')) # to send
        if ser.in_waiting > 0: # to receive 
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

except KeyboardInterrupt:
    print('close serial')
    ser.write(f"vs: 000 000\n".encode('utf-8')) # to send
    ser.close()
