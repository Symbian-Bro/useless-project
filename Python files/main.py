import time
import keyboard
import serial
import serial.tools.list_ports as listing

def port_finder():
    port_name = None
    ports = listing.comports()
    for port in ports:
        if (("Arduino" in port.description) or ("USB Serial" in port.description) or ("ttyUSB" in port.device)):
            port_id = port.device
            break
    return port_id

data = serial.Serial(port_id, 9600, timeout=timeout)
time.sleep(2)

def serial_reader(data,timeout=1):
    while(True):
        if data.in_waiting > 0:
            try:
                line = int(data.readline().decode('utf-8').strip())
                return line
            except ValueError:
                continue

current_time = time.time()
value = []
while (time.time() - current_time < 60):
    value.append(serial_reader(data))

threshold = int(sum(value) / len(value))

while (True):
    current_value = serial_reader(data)
    if current_value > (threshold+100):
        flag = 1
    elif current_value < (threshold-100):
        flag = 0
    else:
        pass