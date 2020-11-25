import pytesseract
import time
from PIL import ImageGrab, Image
from pynput.keyboard import Key, KeyCode, Listener, Controller

pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe"

class Data:
    count = 0
    tl = ()
    br = ()


def on_click(x, y, button, pressed):
    if Data.count == 2:
        return False

    if pressed: 
        Data.count += 1
        if Data.count == 1:
            Data.tl = (x,y)

        else:
            Data.br = (x,y)

def on_press(key):
    if key == KeyCode.from_char("p"):
        print("getting coords")
        return False

with Listener(on_press=on_press) as listener:
    listener.join()

from pynput.mouse import Button, Listener
with Listener(on_click=on_click) as listener:
    listener.join()

print(Data.tl, Data.br)

im = ImageGrab.grab(bbox=Data.tl + Data.br)
para = pytesseract.image_to_string(im)
print(para.strip("|"))
im.show()

keyboard = Controller()
time.sleep(3)
for c in para:
    keyboard.press(c)
    time.sleep(0.1)



