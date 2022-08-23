# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,\
    여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

def good_customer(info):
    info_lst=list(info.split(','))
    info_dic={'아이디':[],'나이':[],'전화번호':[],'성별':[],'지역':[],'구매횟수':[]}
    idx=[]
    for i in range(len(info_lst)):
        if i%6==0 :
            info_dic['아이디'].append(info_lst[i])
        elif i%6==1 :
            info_dic['나이'].append(info_lst[i])
        elif i%6==2 :
            if info_lst[i] =='x':
                info_dic['전화번호'].append('000-0000-0000')
            else:
                info_dic['전화번호'].append(info_lst[i])
        elif i%6==3 :
            info_dic['성별'].append(info_lst[i])
        elif i%6==4 :
            info_dic['지역'].append(info_lst[i])
        else :
            info_dic['구매횟수'].append(info_lst[i])
            if int(info_lst[i])>=8:
                idx.append(i//6)
    print(info_dic)
    for i in idx:
        if info_dic['전화번호'][i] != '000-0000-0000' :
            print(f'''할인 쿠폰을 받을 회원정보 아이디:{info_dic['아이디'][i]}, 나이:{info_dic['나이'][i]}, \
전화번호:{info_dic['전화번호'][i]}, 성별:{info_dic['성별'][i]}, 지역:{info_dic['지역'][i]}, 구매횟수: {info_dic['구매횟수'][i]}''')
        

good_customer(info)