
print("구구단 몇단을 계산할까요? :")
gogodan = int(input())

print(f"구구단 {gogodan}을 입력합니다.")
for i in range(1,10):

    print("{0} X {1} = {2}".format(gogodan,i,i*gogodan))
