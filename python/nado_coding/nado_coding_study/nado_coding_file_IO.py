"""score_file = open("score.txt","w",encoding = "utf8")
print("수학 : 0 ",file = score_file)
print("영어 : 0 ",file = score_file)
score_file.close()"""

'''score_file = open("score.txt","a",encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 10")
score_file.close()'''

"""score_file = open("score.txt","r",encoding = "utf8")
print(score_file.read())
score_file.close()"""

'''score_file = open("score.txt","r",encoding = "utf8")
print(score_file.readline(), end = "")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()'''
''''
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어올 내용이 없으면?
        break # 반복문 탈출
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
score_file.close()
'''
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines :
    print(line, end="")
score_file.close()