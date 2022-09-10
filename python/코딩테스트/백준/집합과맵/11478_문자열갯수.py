s=input()
cnt=1
lst=[]
while cnt <= len(s):
    for i in range(len(s)):
        lst.append(s[i:i+cnt])
    cnt+=1
print(len(set(lst)))
