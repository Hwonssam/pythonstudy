from tkinter import *
from tkinter import ttk

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

values= [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초목록제목설정


readonly_combobox = ttk.Combobox(root, height = 10, values=values ,state="readonly")
readonly_combobox.current(0) #0번째 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
btn= Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()