import random
com = random.randint(1,3)

def rpc(my_choice):
    dic = {"가위":1, "바위":2, "보":3}
    player = int(dic[my_choice])
    rpc_div = int((com/player)*6)
    if rpc_div == 6 :
        rpc_result = "비겼습니다."
    elif rpc_div == 18 or 3 or 4 :
        rpc_result = "이겼습니다."
    elif rpc_div == 12 or 9 or 2 :
        rpc_result = "졌습니다."


    key_list = list(dic.keys())
    val_list = list(dic.values())
    comp_choice = key_list[val_list.index(com)]
    print("당신은 ",my_choice)
    print("컴퓨터는 ",comp_choice)
    print("당신은 ", rpc_result)
    print(com, player, rpc_div)
my= input("가위, 바위, 보 중 하나를 입력하세요: ")
rpc(my)