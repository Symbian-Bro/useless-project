import serial
import time

delay_minutes = 5 #Time after which the threshold will be set (Refer to Logic)
time.sleep(delay_minutes * 60)
def serial_reader(port,bitrate=9600,timeout=1):
    data = serial.Serial(port, bitrate, timeout=timeout)
    time.sleep(2)

    while(True):
        if data.in_waiting > 0:
            try:
                line = int(data.readline().decode('utf-8').strip())
                return line
            except ValueError:
                continue

threshold = serial_reader('/dev/ttyUSB0', 9600)

while (True):
    y = serial_reader('/dev/ttyUSB0', 9600)
    if y > (threshold+100):
        #Slow down
    elif y < (threshold-100):
        #Speed up
    else:
        #I don't know what to put here


