#m,n 입력오류 예외처리 
n = 0
while n != True and n < 1 or n == 1  : # n이 1일때 True가 되어 입력되고 넘어가는 경우가 있어 n == 1 조건 추가
    try :
        n = int(input("첫 번째 수 입력 : "))
        if n <= 1 : # n이 1혹은 음수일 경우 메세지 except메세지가 출력되지않아 따로 조건문 추가

            print("1보다 큰 정수를 입력해주세요.")
    except ValueError:
        print("1보다 큰 정수를 입력해주세요.")
m = 0        
while m != True and m < 1 or m == 1:
    try :
        m = int(input("두 번째 수 입력 : "))
        if m <= 1 :
            print("1보다 큰 정수를 입력해주세요.")
    except ValueError:
        print("1보다 큰 정수를 입력해주세요.")

def count_prime_number(n, m) :
    prime_list = []   
    for i in range(n,m+1) :  #n~m까지 소수 리스트안에 넣기
        prime_list.append(i)
        for j in range(2,m+1) :
            if i%j == 0 and i != j :# m이 소수일때 자기자신으로 나눴다고 리스트에 사라지지않도록 조건 추가
                try:
                    prime_list.remove(i) # 2부터 m-1까지 자기자신이 아닌 수로 나누어진다면 소수가 아니므로 리스트에서 제거
                except : # 같은 수를 리스트에서 제거하려 할 때 오류가 뜨므로 예외처리
                    pass
#마지막 소수리스트 확인용    print(prime_list)
    print(f"{n}에서 {m}까지 소수의 개수: {len(prime_list)}개") #len 소수리스트의 개수 = 소수가 아닌 수가 걸러지고 남은 소수 개수
count_prime_number(n,m)
