import win32api, win32con, random, time

print("Close program to stop mouse movement. (ALT+F4 recommended)")

while True:
    cursorPos = win32api.GetCursorPos() # Gets current cursor position (x, y)
    cursorPosX = cursorPos[0] # Gets X coordinate of cursor
    cursorPosY = cursorPos[1] # Gets Y coordinate of cursor
    cursorIncX = random.randint(-1,1) # Random integer to increment X value
    cursorIncY = random.randint(-1,1) # Random integer to increment Y value
    cursorPosX += cursorIncX # Sets new X coordinate
    cursorPosY += cursorIncY # Sets new Y coordinate
    win32api.SetCursorPos((cursorPosX, cursorPosY)) # Changes cursor position
    time.sleep(0.05) # Waits 0.05s, otherwise the program won't work properly. Can be adjusted.