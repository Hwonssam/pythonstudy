while True :
    try :
        dan=int(input("몇단?: "))
        break
    except ValueError:
        print("1~9중의 숫자를 입력해주세요")
print(dan,"단")
for i in range(10) :
    if i%2 == 1 and dan*i <=50 :
        print(f"{dan} X {i} = {i*dan}")
