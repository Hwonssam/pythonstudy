from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

label1 = Label(root, text="안녕하세요")
label1.pack()

photo= PhotoImage(file="python\gui_basic\img.png")
label2 = Label(root, image= photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    global photo2
    photo2 = PhotoImage(file="python\gui_basic\img2.png")
    label2.config(image= photo2)

btn= Button(root, text="클릭", command= change)
btn.pack()


label3 = Label(root, text="안녕하세요")
label3.pack()


root.mainloop()