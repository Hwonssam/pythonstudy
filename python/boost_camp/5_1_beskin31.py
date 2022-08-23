import random
n=[28]
def bs31_my():
    global n
    while True:
        try:
            my = list(map(int,input("My turn - 숫자를 입력하세요(다음 3개까지): ").split()))
        except ValueError:
            print("숫자를 입력해주세요")
            continue
        if len(my) >3:
            print("숫자를 너무 많이 입력했습니다.")
        elif my[0] != n[-1]+1:
            print("마지막 불린 숫자 다음 숫자를 불러주세요")
        elif len(my)==2 and my[0]!=my[1]-1 :
            print("숫자를 순서대로 불러주세요")
        elif len(my)==3 and my[0]!=my[1]-1 or len(my)==3 and my[1]!=my[2]-1 :
            print("숫자를 순서대로 불러주세요")
        else:
            n += my
            if 31 in n:
                print(f"현재 숫자 : 31")
                print("당신이 31을 불렀으므로 당신의 패배")
                break
            print(f"현재 숫자 : {n[-1]}")
            break
def bs31_com():
    com_num = random.randint(1,3)
    for i in range(com_num):
        n.append(n[-1]+1)
        print(f"컴퓨터 : {n[-1]}")
        if 31 in n:
            print("컴퓨터가 31을 불렀으므로 당신의 승리!!")
            break
    if 31 in n:
        pass
    else:
        print(f"현재 숫자 : {n[-1]}")
while n[-1]<31 :
    bs31_my()
    if 31 in n:
        break
    bs31_com()
    