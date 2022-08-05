#훤님

def count_word(a,b):
    with open("new.txt", "w", encoding="utf8") as new_file :
        new_file.write(a)
    with open("new.txt", "r", encoding="utf8") as new_file :
        lines = new_file.read()
        print(lines.count(b))
count_word("안녕하세요.반갑습니다. 파이썬 공부는 정말 재밌습니다!","습니다")