def after_100(month,date,day):
    month_dates=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    date_100=date+99
    month_100 = month
    while True:
        if date_100-month_dates[month_100] < 1:
            break
        date_100 = date_100-month_dates[month_100]
        month_100 +=1
        if month_100 >=13:
            month_100-=12
    days=[0,"월","화","수","목","금","토","일"]
    day_100=days.index(day)+99
    while day_100 >7:
        day_100=day_100-7
    day_100=days[day_100]
    print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {month_100}월 {date_100}일 {day_100}요일")

after_100(6,21,"월")
