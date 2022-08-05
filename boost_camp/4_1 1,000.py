#훤님

def comma(num):
    num=list(str(num))
    cnt =0
    for i in num :
        cnt +=1
        if cnt %4 == 0 and cnt !=0 :
            num.insert(-cnt+1,',')
    answer=''
    for j in num :
        answer += j
    print(answer)

num = input('쉼표찍고 싶은 수를 입력하세요: ')
comma(num)