stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
def stock_profit(stocks, sells):
    stocks_lst =[]
    earning_lst=[]
    for i in range(len(sells)):
        stocks_lst.append(list(stocks.split(','))[i].split('/'))
        earning_lst.append([stocks_lst[i][0],f'{(sells[i]-int(stocks_lst[i][2]))*100/int(stocks_lst[i][2]):.3}'])
    earning_lst.sort(key = lambda earning_lst: float(earning_lst[1]),reverse=True)
    for i in range(len(earning_lst)):
        print(f'{earning_lst[i][0]}의 수익률 : {earning_lst[i][1]}')

stock_profit(stocks, sells)
