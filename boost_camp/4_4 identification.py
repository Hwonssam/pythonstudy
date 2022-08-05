#훤님

def check_id(a):
    if a[7] =='1' or a[7] =='3':
        sex = '남자'
    elif a[7] =='2' or a[7] =='4':
        sex = '여자'
    else :
        print("잘못된 번호입니다\n올바른 번호를 넣어주세요")
    if int(a[0])*10+int(a[1]) >=0 and int(a[0])*10+int(a[1]) <= 22:
        check_birth = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if check_birth == 'o' and a[7] != '3' and a[7] !='4' :
            print("잘못된 번호입니다\n올바른 번호를 넣어주세요")
        else :
            print(f"{a[0:2]}년{a[2:4]}월 {sex}")
    else :
            print(f"{a[0:2]}년{a[2:4]}월 {sex}")
a = "000629-2222222"
check_id(a)
