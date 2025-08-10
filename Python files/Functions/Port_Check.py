import serial.tools.list_ports as listing

def port_finder():
    port_name = None
    ports = listing.comports()
    for port in ports:
        if "Arduino" in port.description:
            port_id = port.device
            break
    return port_id