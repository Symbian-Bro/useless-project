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

def capture_keypress(event):
    log_file = "capture.txt"
    with open(log_file, "a", encoding="utf-8") as f:
        if event.name == "space":
            f.write(" ")
        elif event.name == "enter":
            f.write("\n")
        elif event.name == "backspace":
            f.write("[BACKSPACE]")
        elif len(event.name) > 1:
            f.write(f"[{event.name.upper()}]")
        else:
            f.write(event.name)

    keyboard.hook(capture_keypress,suppress=True)

                                 #Main program

if __name__ == "__main__":
 port_id = port_finder()
 if not port_id:
     print("Please check your Arduino connection.")
     sys.exit()

 data = serial.Serial(port_id, 9600, timeout=1)
 time.sleep(2)

 print("Please wait for 60 seconds...")
 current_time = time.time()
 value = []
 while (time.time() - current_time < 60):
     value.append(serial_reader(data))

 threshold = int(sum(value) / len(value))

 keyboard_thread = threading.Thread(target=word_counter, daemon=True)
 keyboard_thread.start()
 print("You can start typing now...")

 while (True):
     current_value = serial_reader(data)
     if current_value > (threshold+100):
         flag = 1
     elif current_value < (threshold-100):
         flag = 0
     else:
         pass

 if (flag==1):
     if (word_count>5):
         print("Word count exceeded 5, please wait 60 seconds to type more.")
         crnt_time = time.time()
         while (time.time() - crnt_time < 60):
             event = capture_keypress(event)
         print("You can type again now.")
 elif (flag==0):
     if (word_count>12):
         print("Word count exceeded 12, please wait 60 seconds to type more.")
         crnt_time = time.time()
         while (time.time() - crnt_time < 60):
             event = capture_keypress(event)
         print("You can type again now.")
 else:
     pass