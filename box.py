import win32gui, win32api, threading, time
#from pynput.mouse import Listener

dc = win32gui.GetDC(0)
monitor = (0, 0, 1600, 900)

red = win32api.RGB(255, 0, 0) # red

class Box:
    grabbing = True
    sx, sy = 0, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0

def draw(): # draw the box being dragged
    while Box.grabbing: 
        dis = 1

        for i in range((Box.max_x-Box.min_x+1)//dis):
            win32gui.SetPixel(dc, Box.min_x+dis*i, Box.min_y, red)
            win32gui.SetPixel(dc, Box.min_x+dis*i, Box.max_y, red)

        for i in range((Box.max_y-Box.min_y)//dis):
            win32gui.SetPixel(dc, Box.min_x, Box.min_y+dis*i, red)
            win32gui.SetPixel(dc, Box.max_x, Box.min_y+dis*i, red)

        time.sleep(0.1) # stops lines glitching as much

def on_click(x, y, button, pressed):
    if pressed: # get the starting point
        Box.sx, Box.sy = x, y 
        Box.min_x = x
        Box.min_y = y

        threading.Thread(target=draw).start()
    
    else: # get the finishing point
        Box.max_x = x
        Box.max_y = y
        Box.grabbing = False
        return False # exit listener

def on_move(x, y):
    # if being dragged top left to bottom right as intended, the max x and y will be the mouse pos
    Box.max_x = x
    Box.max_y = y

    # dragging top right to bottom left
    if Box.sx > Box.max_x and Box.sy < Box.max_y:
        Box.min_x, Box.max_x = Box.max_x, Box.sx
    
    # dragging bottom left to top right
    elif Box.sx < Box.max_x and Box.sy > Box.max_y:
        Box.min_y, Box.max_y = Box.max_y, Box.sy

    # dragging bottom right to top left
    elif Box.sx > Box.max_x and Box.sy > Box.max_y:
        Box.min_x, Box.max_x = Box.max_x, Box.sx
        Box.min_y, Box.max_y = Box.max_y, Box.sy
"""
with Listener(on_click=on_click, on_move=on_move) as listener:
    listener.join()
"""