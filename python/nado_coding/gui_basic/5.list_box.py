from tkinter import *

root= Tk()
root.title("Hwon GUI")
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표

listbox = Listbox(root, selectmode="extended", height=0) #height=보이는 수
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2, "바나나")
listbox.insert(END,"수박") #END 마지막에 추가
listbox.insert(END,"포도")
listbox.pack()


def btncmd():
    #삭제
    #listbox.delete(0) #0은 맨앞 삭제

    #갯수확인
    #print("리스트에는", listbox.size(), "개가 있어요")
    
    #항목 확인
    #print("1번쨰부터 3번째까지의 항목: ", listbox.get(0,2))

    #선택된 항목확인(위치로 반환)
    print("선택된 항목: ", listbox.curselection())
btn= Button(root, text = "클릭", command=btncmd)
btn.pack()

root.mainloop()