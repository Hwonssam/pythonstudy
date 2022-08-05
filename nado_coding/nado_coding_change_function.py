def profile(name="지훤", age="30", *language) :
    print("이름: {0} 나이:{1}".format(name,age), end=" ")
    for rang in language :
        print(f" {rang} ", end = "")
profile("지훤",30, "파이썬", "자바")
