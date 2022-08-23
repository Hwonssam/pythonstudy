import keyboard
import time
from PIL import ImageGrab

def screenshot():
    #2022년 6월 1일 10시 20분 40초 -> _20220601_102040
    curr_time = time.strftime("_%y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(1)) #imge_20220601_102040.png

keyboard.add_hotkey("F9",screenshot)

keyboard.wait("esc")