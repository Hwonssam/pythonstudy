from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

txt= Text(root, width= 30, height = 5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e= Entry(root, width = 30) #한줄로만
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END)) #1.0 = 1번째줄 0번째 칼럼위치부터 가져와라
    print(e.get())
 #내용삭제
    txt.delete("1.0", END)
    e.delete(0,END)
btn= Button(root, text = "클릭", command=btncmd)
btn.pack()

root.mainloop()