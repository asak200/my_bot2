#!/user/bin/env python3

import serial
import time, random

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(2.)
ser.reset_input_buffer()

print("Serial initilized")

try:
    while True:
        time.sleep(0.5)
        i = random.randint(0,1)
        ser.write(f"val is: {i}\n".encode('utf-8')) # to send
        if ser.in_waiting > 0: # to receive 
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

except KeyboardInterrupt:
    print('close serial')
    ser.close()
