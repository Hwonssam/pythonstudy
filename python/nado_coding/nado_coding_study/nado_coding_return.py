def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 입금 후 잔액 정보 반환
    
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금
print(balance) # 현재 잔액

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance # 기존 잔액 반환
        
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금

# 출금 시도
balance = withdraw(balance, 2000) # 2000원 출금 시도 시 잔액이 부족하므로 실패
balance = withdraw(balance, 500) # 500원 출금 시도 시 성공
print(balance) # 현재 잔액

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 출금 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 반환
    
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))