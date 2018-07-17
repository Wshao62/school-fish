import serial

try:
    ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=2)
except:
    print("沒設備")
    exit()

# ser.write()
# ser.read()
# ser.readline()