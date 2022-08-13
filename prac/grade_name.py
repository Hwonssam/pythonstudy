name,score=input("이름과 점수를 입력하세요: ").split()
def grader(name,score):
    score=int(score)
    if score <60 :
        grade = "F"
    elif score<65 :
        grade = "D"
    elif score<70 :
        grade = "D+"
    elif score<75 :
        grade = "C"
    elif score<80 :
        grade = "C+"
    elif score<85 :
        grade = "B"
    elif score<90 :
        grade = "B+"
    elif score<95 :
        grade = "A"
    elif score<=100 :
        grade = "A+"
    print(f"학생이름:{name}",f"점수:{str(score)}",f"학점:{grade}",sep='\n')
grader(name,score)
