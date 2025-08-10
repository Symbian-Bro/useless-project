import serial
import time

delay_seconds = 300 #Time after which the threshold will be set (Refer to Logic)
time.sleep(delay_seconds)

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
    current_value = serial_reader('/dev/ttyUSB0', 9600)
    if current_value > (threshold+100):
        flag = 1
    elif current_value < (threshold-100):
        flag = 0
    else:
        pass


