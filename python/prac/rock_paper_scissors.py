import random
rpc_com = random.randint(0, 2)
if rpc_com == 0 :
    rpc_com = "가위"
elif rpc_com == 1 :
    rpc_com = "바위"
elif rpc_com == 2 :
    rpc_com = "보"

rpc_user = input("가위,바위,보!(이 중하나를 입력하세요):")

if rpc_com == rpc_user :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("비겼습니다.")
elif rpc_com == "가위" and rpc_user == "바위" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 이겼습니다.")
elif rpc_com == "보" and rpc_user =="가위" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 이겼습니다.")
elif rpc_com == "바위" and rpc_user =="보" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 이겼습니다.")
elif rpc_com == "가위" and rpc_user =="보" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 졌습니다.")
elif rpc_com == "바위" and rpc_user =="가위" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 졌습니다.")
elif rpc_com == "보" and rpc_user =="바위" :
    print("컴퓨터:",f"{rpc_com}","도전자: " f"{rpc_user}","입니다")
    print("당신은 졌습니다.")