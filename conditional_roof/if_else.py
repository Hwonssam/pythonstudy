birthyear = int(input("당신이 태어난 연도를 입력하세요: "))
age = 2021 - birthyear + 1
message= ""


if age <26 and age >=20 :
    message = "대학생"
elif age >=17 and age < 20 : 
    message = "고등학생"
elif age >=14 and age < 17 : 
    message = "중학생"
elif age >=8 and age < 14 : 
    message = "초등학생"
else :
    print("학생이 아닙니다.")

print(message)
