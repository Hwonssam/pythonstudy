s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
correct_ans = [3,2,4,2,5,2,4,3,1,2]
def grader(s,correct_ans):
    name=[]
    studen_ans=[]
    score=[]
    for i in s:
        name.append(i.split(',')[0])
        studen_ans.append(i.split(',')[1])
    for i in studen_ans:
        a=0
        for j in range(len(correct_ans)) :
            if correct_ans[j]==int(i[j]):
                a+=10
        score.append(a)
    dic={}
    for i in range(len(name)):
        dic[name[i]] = score[i]
    print(dic)
    score= score.sorted()
grader(s,correct_ans)