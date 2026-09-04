import serial
import time

ser = serial.Serial("COM7", 115200)

while True:
    ser.write(b"25.3,61.2\n")
    print("TX: 25.3,61.2")
    time.sleep(5)
