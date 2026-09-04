import serial

ser = serial.Serial("COM8", 115200)

while True:
    data = ser.readline().decode().strip()
    print("RX:", data)
