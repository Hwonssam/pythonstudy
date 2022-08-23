from tkinter import *

root= Tk()
root.title("제목없음 - Window 메모장")
#root.geometry("640x480") #가로 *세로
root.geometry("640x480+300+100") #가로 *세로 +x좌표 +y좌표


def create_new_file():
    with open("mynote.txt", "r", encoding="utf8") as my_note :
        txt.insert(END, my_note.read())
def save_file():
    with open("mynote.txt", "w", encoding="utf8") as my_note :
        my_note.write(txt.get("1.0",END))

menu = Menu(root)
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")
txt= Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)

txt.insert(END, "")



menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=create_new_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit) #종료
menu.add_cascade(label="파일", menu=menu_file)

menu_lang = Menu (menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_lang)

menu_l = Menu (menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_l)

menu_la = Menu (menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_la)

menu_lan = Menu (menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_lan)

root.config(menu=menu)
scrollbar.config(command=txt.yview)

root.mainloop()