def solution(s):
    s=list(s)
    for j in range(len(s)-1) :
        for i in range(len(s)-1) : 
            try:
                if s[i] == s[i+1]:
                    s.remove(s[i])
                    s.remove(s[i])
            except :
                pass
            if s==None:
                break
        if s==None:
            break
    if s == []:
        answer = 1
    else :
        answer = 0
    print(s,answer)
    return answer
s='aaavvaacca'
solution(s)