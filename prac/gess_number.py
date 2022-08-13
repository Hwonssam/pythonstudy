import random
guess_number = random.randint(1,100)
print("숫자를 맞춰보세요 (1~100)")
user_number = int(input())

while (user_number is not guess_number) :
    if user_number > guess_number :
        print("숫자가 너무 큽니다.")
        print("다시 숫자를 입력해주세요.(1~100)")
    else :
        print("숫자가 너무 작습니다.")
        print("다시 숫자를 입력해주세요.(1~100)")
    user_number = int(input())
else: 
    print("정답입니다.","입력한 숫자는",str(guess_number),"입니다")
