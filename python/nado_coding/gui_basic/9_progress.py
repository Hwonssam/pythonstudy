from tkinter import *
from tkinter import ttk as ttk
import time

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

#progressbar = ttk.Progressbar(root, maximum= 100, mode = "indeterminate")
""" progressbar = ttk.Progressbar(root, maximum= 100, mode = "determinate") #bar 차게하기
progressbar.start(10) #10 ms마다 움직임
progressbar.pack()


def btncmd():
   progressbar.stop() #작동중지



btn= Button(root, text = "중지", command=btncmd)
btn.pack()
 """
p_var2= DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
   for i in range(101): 
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #progress bard의 값설정
        progressbar2.update() # UI 업데이트
        print(p_var2.get())
btn= Button(root, text = "시작", command=btncmd2)
btn.pack()

root.mainloop()