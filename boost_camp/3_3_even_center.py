#m,n 예외처리
#n이 0일때에는 오류가 나지 않으므로 except의 메세지는 뜨지 않음.
n = 0
while n != True and n <= 0 :
    try :
        n = int(input("첫 번째 수 입력 : "))
        if n <= 0 :
            print("0보다 큰 정수를 입력해주세요.")
    except ValueError:
        print("0보다 큰 정수를 입력해주세요.") 
m = 0
while m != True and m <= 0 :
    try :
        m = int(input("두 번째 수 입력 : "))
        if m <= 0 :
            print("0보다 큰 정수를 입력해주세요.")
    except ValueError:
        print("0보다 큰 정수를 입력해주세요.")
        
def find_even_number(n,m) :
    for i in range (n,m+1) :
        if i%2 != 0 : #continue로 홀수 건너뛰기
            continue
        print(f"{i} 짝수")
        if i == (n+m)/2:
            print(f"{i} 중앙값")
find_even_number(n,m)