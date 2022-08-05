
month_income=input("당신의 월급은?(만원 단위로 입력하세요):")
annual_income=int(month_income)*12
if annual_income <= 1200:
    after_tax = annual_income*0.94
elif annual_income <= 4600:
    after_tax = annual_income*0.85
elif annual_income <= 8800:
    after_tax = annual_income*0.76
elif annual_income <= 15000:
    after_tax = annual_income*0.65
elif annual_income <= 30000:
    after_tax = annual_income*0.62
elif annual_income <= 50000:
    after_tax = annual_income*0.6
elif annual_income < 50000:
    after_tax = annual_income*0.58
print("세전연봉:","%0.2f" % annual_income,"만원")
print("세후연봉:","%0.2f" % after_tax,"만원")