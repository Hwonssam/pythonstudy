
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
def sales_management(member_names, member_records) :
    lst=[]
    for i in range(len(member_records)):
        member_records[i] = sum(member_records[i])/len(member_records[i])
        lst.append([member_names[i],member_records[i]])
    lst.sort(key= lambda lst:int(lst[1]*100),reverse=True)
    for g in range(2):
        if lst[g][1] > 5:
            print(f'보너스 대상자: {lst[g][0]}')
    print('='*25)
    for k in range(-2,0):
        if lst[k][1] <= 3:
            print(f'면접 대상자: {lst[k][0]}')


sales_management(member_names, member_records)