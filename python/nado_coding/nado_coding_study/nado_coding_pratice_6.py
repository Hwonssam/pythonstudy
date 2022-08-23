class SoldoutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self) :
        return self.msg

chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    try:
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1 :
            print("잘못된 값을 입력하였습니다.")
            raise ValueError    
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1 # 대기번호 증가
            chicken -= order # 주문 수 만큼 남은 치킨 감소
        if chicken == 0 :
            raise SoldoutError("치킨이 모두 소진되었습니다.")
    except ValueError :
        print("잘못된 값을 입력하였습니다.")
    except SoldoutError as err: 
        print(err)
        print("오늘 장사를 마칩니다")
        break    
    
        

