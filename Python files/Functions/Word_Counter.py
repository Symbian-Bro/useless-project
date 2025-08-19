import keyboard

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