from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

label1= Label(root, text= "메뉴를 선택하세요").pack()
Label(root, text= "음료를 선택하세요").pack()
buger_var = IntVar()
btn_buger1 = Radiobutton(root, text = "햄버거", value=1, variable=buger_var)
btn_buger1.select()
btn_buger2 = Radiobutton(root, text = "치즈버거", value=2, variable=buger_var)
btn_buger3 = Radiobutton(root, text = "치킨 버거", value=3, variable=buger_var)

btn_buger1.pack()
btn_buger2.pack()
btn_buger3.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "콜라",  value = "콜라",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "사이다",  value = "사이다",variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(buger_var.get()) #햄버거중 선택된 라디오 항목 값(value) 츌력
    print(drink_var.get()) 
btn= Button(root, text = "주문", command=btncmd)
btn.pack()

root.mainloop()