import random
def guess_numbers():
    num_list = random.sample(range(1,101),3)
    print(num_list)
    num_list.sort()
    n=num_list[0]
    c=num_list[1]
    m=num_list[2]
    guessed=[]
    cnt=1
    while num_list !=[]:
        print(f"{cnt}차시도")
        guess=int(input("숫자를 예측해보세요 : "))
        if guess in num_list :
            if guess == n:
                print(f"숫자를 맞추셨습니다! {n}은/는 최솟값입니다.")
                num_list.remove(n)
            if guess == c:
                print(f"숫자를 맞추셨습니다! {c}은/는 중간값입니다.")
                num_list.remove(c)
            if guess == m:
                print(f"숫자를 맞추셨습니다! {m}은/는 최댓값입니다.")
                num_list.remove(m)
        elif guess in guessed:
                print("이미 예측에 사용한 숫자입니다")
                cnt -=1
        else: 
            print(f"{guess}는 없습니다")
            if cnt==5 and n in num_list and guess<n or cnt>=10 and n in num_list and guess<n:
                print(f"최솟값은 {guess}보다 큽니다.")
            elif cnt==5 and n in num_list and guess>n or cnt>=10 and n in num_list and guess>n:
                print(f"최솟값은 {guess}보다 작습니다.")
            elif cnt==5 and m in num_list and guess>m or cnt>=10 and m in num_list and guess>m:
                print(f"최댓값은 {guess}보다 작습니다.")
            elif cnt==5 and m in num_list and guess<m or cnt>=10 and m in num_list and guess<m:
                print(f"최댓값은 {guess}보다 큽니다.")
            elif cnt==5 and c in num_list and guess<c or cnt>=10 and c in num_list and guess<c:
                print(f"중앙값은 {guess}보다 큽니다.")
            elif cnt==5 and c in num_list and guess>c or cnt>=10 and c in num_list and guess>c:
                print(f"중앙값은 {guess}보다 작습니다.")
        guessed.append(guess)
        cnt+=1
    print(f"""게임종료
{cnt-1}번 시도만에 예측 성공!!""")
guess_numbers()

