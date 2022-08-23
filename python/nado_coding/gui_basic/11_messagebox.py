import tkinter.messagebox as msgbox
from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

#기차예매 시스템이라 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showwarning("경고", "해당 좌성은 매진되었습니다.")
def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당좌석은 유아 동반석입니다. 예매하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류 입니다. 다시 시도하시겠습니까?")
def yesno():
    msgbox.askyesno("예 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")
def yesnocancel():
    response = msgbox.askyesnocancel(title= None, message="예매 내역이 저장되지 않았습니다.\n저장후 종료하시겠습니까? ")
    #네: 저장후 종료
    #아니요: 저장안하고 종료
    #취소: 프로그램 종료 취소(현재화면에서 계속 작업)
    print("응답", response) # True, False, None -> 1.예 0.아니요 그외 취소
    if response == 1 :
        print("예")
    if response == 0 :
        print("아니요")
    if response == None :
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()

Button(root, command=retrycancel, text="예 아니오").pack()
Button(root, command=yesno, text="예 아니오").pack()

Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()