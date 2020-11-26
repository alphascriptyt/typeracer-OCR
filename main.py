import pytesseract
import time
from PIL import ImageGrab, Image, ImageOps
from pynput.keyboard import Key, KeyCode, Listener, Controller
import box 

pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe" # location of the tesseract exe

def on_press(key):
    if key == KeyCode.from_char("p"):
        return False

with Listener(on_press=on_press) as listener:
    listener.join()

from pynput.mouse import Button, Listener

with Listener(on_click=box.on_click, on_move=box.on_move) as listener:
    listener.join()

box.on_move(box.Box.max_x, box.Box.max_y) # format coordinates
im = ImageGrab.grab(bbox=(box.Box.min_x, box.Box.min_y, box.Box.max_x, box.Box.max_y)) # grab the image
para = pytesseract.image_to_string(im).replace("|", "I").replace("\n", " ").replace("”", '"') # convert image to text
print(para)

keyboard = Controller()
time.sleep(2)
for c in para:
    keyboard.press(c)
    time.sleep(0.01)

im.show()


