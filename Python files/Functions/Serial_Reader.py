import serial
import time
import numpy as po

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

port_id = port_finder()

current_time = time.time()
value = []
while (time.time() - current_time < 60):
    value.append(serial_reader(port_id, 9600))

threshold = po.mean(value)

while (True):
    current_value = serial_reader(port_id, 9600)
    if current_value > (threshold+100):
        flag = 1
    elif current_value < (threshold-100):
        flag = 0
    else:
        pass


