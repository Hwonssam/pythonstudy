#훤님

def visitors_book(name_n_phone_num):
    with open("visitors_book.txt", "w", encoding="utf8") as visitors_book_file :
        visitors_book_file.write(name_n_phone_num)
    with open("visitors_book.txt", "r", encoding="utf8") as visitors_book_file :
        lines = (visitors_book_file.readlines())
        for i in range(len(lines)) :
            lines2 = lines[i].rstrip('\n').split(',')
            if lines2[1].startswith('010')==False or \
                lines2[1][3]!='-'or lines2[1][8]!='-'or len(lines2[1]) !=13:
                print(f" 잘못 쓴 사람 : {lines2[0]}\n 잘못 쓴 번호 : {lines2[1]}\n")

visitors_book("""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333""")