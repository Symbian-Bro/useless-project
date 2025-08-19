import time
import keyboard
import serial
import serial.tools.list_ports as listing
import threading
import sys

word_count = 0
buffer = ""

def port_finder():
    port_name = None
    ports = listing.comports()
    for port in ports:
        if (("Arduino" in port.description) or ("USB Serial" in port.description) or ("ttyUSB" in port.device)):
            port_id = port.device
            break
    return port_id

def serial_reader(data,timeout=1):
    while(True):
        if data.in_waiting > 0:
            try:
                line = int(data.readline().decode('utf-8').strip())
                return line
            except ValueError:
                continue

def word_counter():
    global word_count, buffer
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "space":
                if buffer:
                    word_count = word_count + 1
                    buffer = ""
            elif len(key) == 1:  
                buffer = buffer + key
            elif key == "enter":
                if buffer:
                    word_count = word_count + 1
                    buffer = ""
            elif key == "backspace":
                buffer = buffer[:-1] if buffer else ""
            else:
                pass
    return word_count

                                 #Main program
port_id = port_finder()
if not port_id:
    print("Please check your Arduino connection.")
    sys.exit()

data = serial.Serial(port_id, 9600, timeout=timeout)
time.sleep(2)

print("Please wait for 60 secoonds...")
current_time = time.time()
value = []
while (time.time() - current_time < 60):
    value.append(serial_reader(data))

threshold = int(sum(value) / len(value))