import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1,11): #2초간격으로 10개 저장
    img = ImageGrab.grab()
    img.save("image{}.png".format(i)) # 파일로 저장 (image1.png~)
    time.sleep(2) #2초단위