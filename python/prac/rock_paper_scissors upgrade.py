re_game = "네"
com_win = 0
user_win = 0
while re_game== "네" :
    import random
    com_value = random.randint(0, 2)
    if com_value == 0 :
        com_value = "가위"
    elif com_value == 1 :
        com_value = "바위"
    elif com_value == 2 :
        com_value = "보"

    user_value = input("가위,바위,보!(이 중하나를 입력하세요):")
    if com_value == user_value :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("비겼습니다.")
    elif com_value == "가위" and user_value == "바위" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("이겼습니다.")
        user_win += 1
    elif com_value == "보" and user_value =="가위" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("이겼습니다.")
        user_win += 1
    elif com_value == "바위" and user_value =="보" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("이겼습니다.")
        user_win += 1
    elif com_value == "가위" and user_value =="보" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("졌습니다.")
        com_win += 1
    elif com_value == "바위" and user_value =="가위" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("졌습니다.")
        com_win += 1
    elif com_value == "보" and user_value =="바위" :
        print("컴퓨터:",f"{com_value}","도전자: " f"{user_value}","입니다")
        print("졌습니다.")
        com_win += 1
    print("지금까지 결과는 컴퓨터:",f"{com_win}","승"," 도전자:",f"{user_win}","승 입니다.")
    re_game = input("""게임을 이어하시겠습니까?(계속하려면 "네"을 입력):""")
    if re_game != "네" :
        print("게임을 종료합니다. 최종 결과는 컴퓨터:",f"{com_win}","승"," 도전자:",f"{user_win}","승 입니다.")
        break
