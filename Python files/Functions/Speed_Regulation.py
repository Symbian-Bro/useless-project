import time

if (flag==1):
    n = word_counter()
    if (n>5):
        print("Word count exceeded 5, please wait 60 seconds to type more.")
        capture_keypress(event)
        time.sleep(60)
elif (flag==0):
    if (n>12):
        print("Word count exceeded 12, please wait 60 seconds to type more.")
        capture_keypress(event)
        time.sleep(60)
else:
    pass