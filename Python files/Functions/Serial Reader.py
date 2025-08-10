import serial
import time
def serial_reader(port,bitrate=9600,timeout=1):
    data = serial.Serial(port, bitrate, timeout=timeout)
    time.sleep(2)

    while(True):
        if data.in_waiting > 0:
            try:
                line = int(data.readline().decode('utf-8').strip())
                print(f"Received: {line}")
            except ValueError:
                continue