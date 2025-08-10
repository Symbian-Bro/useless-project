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