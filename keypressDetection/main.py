import keyboard
import time

# --------------------- Set restricted keys -----------------
restrictedKey = ["tab", "ctrl", "prtsc "]

# --------------------- Create file names -------------------
timeNow = time.time()
timeNow = str(timeNow).split('.')
timeNow = timeNow[0] + timeNow[1]

# --------------------- Run the program, save files -------------------
while True:
    if keyboard.read_key() in restrictedKey:
        f = open(f"tracking/{timeNow}.txt", "a")
        f.write(str(keyboard.read_key()))