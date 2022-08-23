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
    sorted_name=[]
    for i in s:
        name.append(i.split(',')[0])
        studen_ans.append(i.split(',')[1])
    for i in studen_ans:
        a=0
        for j in range(len(correct_ans)) :
            if correct_ans[j]==int(i[j]):
                a+=10
        score.append(a)
    sorted_score= sorted(score)
    for i in sorted_score:
        sorted_name.append(name[score.index(i)])
        #같은 점수일때 이름이 중복되므로 제거
        name.remove(sorted_name[-1])
        score.remove(i)
    for i in range(1,len(sorted_name)+1):
        #공동1등 가능성
        if sorted_score[-i] == sorted_score[-i+1]:
            print(f"학생: {sorted_name[-i]} 점수: {sorted_score[-i]} {grade}등")
        else:
            grade = i
            print(f"학생: {sorted_name[-i]} 점수: {sorted_score[-i]} {grade}등")
grader(s,correct_ans)