def buss_fare(age,form):
    age=int(age)
    if age <8:
        fare = "무료"
    elif age < 14 :
        fare = "450원"
    elif age < 20 and form =="현금":
        fare = "1000원"
    elif age < 20 and form =="카드":
        fare = "720원"
    elif age < 75 and form =="현금":
        fare = "1300원"
    elif age < 75 and form =="카드":
        fare = "1200원"
    else :
        fare = "무료"
    print(f"나이: {age}세",f"지불유형: {form}", f"버스요금: {fare}",sep='\n')

age= input("나이: ")
form = input("지불방식(현금혹은 카드): ")
buss_fare(age,form)

    