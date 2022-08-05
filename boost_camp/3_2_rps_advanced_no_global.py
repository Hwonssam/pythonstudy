#판수 정하기, 예외처리
while True :
    try:
        games = int(input("선생님, 저와 몇 판을 하시겠습니까?: "))
        break
    except ValueError:
        print("다시 입력해주세요")
#승리,패배(컴퓨터승리),무승부 기본값
(user_win,com_win,draw) = (0,0,0)
#함수 rps 
#com_rps,user_rps는 가위바위보 낸것, _num은 1,2,3
def rps(draw, user_win, com_win):
    import random
    com_num = random.randint(1,3)
    dic={"가위": 1 , "바위":2, "보":3 }
    key_list = list(dic.keys())
    value_list = list(dic.values())
    com_rps = key_list[value_list.index(com_num)]
    #가위바위보 내기, 예외처리
    while True:
        try:
            user_rps = input("가위(0), 바위(1), 보(2) 중 하나를 입력하세요 :")
            if user_rps == "가위" or user_rps == "바위" or user_rps == "보" \
                or user_rps == '0' or user_rps == '1' or user_rps == '2' : #0,1,2 조건
                break
            print("다시 입력해주세요")
        except ValueError:
            pass
    if user_rps == "가위" or user_rps == "바위" or user_rps == "보" :
        user_num = dic[user_rps]
    elif  user_rps == '0' or user_rps == '1' or user_rps == '2' : #0,1,2를 가위바위보로 변환
        user_num = int(user_rps)+ 1
        user_rps = key_list[int(user_rps)]
    #나눗셈을 통해 승,패,무승부 3개의 조건문 설정
    rps_div = int((com_num/user_num)*6)
    if rps_div == 6 :
        rps_result = "비겼습니다."
        draw += 1
    elif rps_div == 18 or rps_div == 3 or rps_div == 4 :
        rps_result = "이겼습니다."
        user_win += 1
    elif rps_div == 12 or rps_div == 9 or rps_div == 2 :
        rps_result = "졌습니다."
        com_win += 1
    print("="*45,"\n"f"#Round{i+1} 컴퓨터: {com_rps} 도전자: {user_rps}",\
    "\n"f"        당신은 {rps_result}\n","="*45)
    return draw, user_win, com_win
#정한 판수(games)만큼 게임 실행
for i in range(games) :
    draw, user_win, com_win = rps(draw, user_win, com_win)
print(f"최종결과 {games}판 컴퓨터:{com_win}승 도전자:{user_win}승 무승부:{draw}번 입니다.")

#보너스 결과창..
if com_win == user_win :
    print("실력이 비등비등하네요.")
elif com_win < user_win :
    print("축하합니다! 이세돌 9단의 복수를 이루었네요.")
else :
    print("안타깝군요... 당신은 인류의 오점을 남기셨습니다...")

