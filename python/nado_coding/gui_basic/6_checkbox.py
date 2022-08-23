from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

chkvar = IntVar() #chkvar에 int형으로 값저장
chkbox= Checkbutton(root, text= "오늘 하루 보지 않기", variable=chkvar)
""" chkbox.select() #자동 선택
chkbox.deselect() #선택 해제 """
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0:체크해제.1: 체크
    print(chkvar2.get())

btn= Button(root, text = "클릭", command=btncmd)
btn.pack()

root.mainloop()