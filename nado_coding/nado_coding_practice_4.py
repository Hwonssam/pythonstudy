'''지금까지 배운 내용을 복습하기 위한 퀴즈를 드리겠습니다. 직접 한 번 풀어보시고 나서 정답을 확인해주세요.
Quiz) 표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
 남자 : 키(m) * 키(m) * 22
 여자 : 키(m) * 키(m) * 21
조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight 
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시
(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.'''
(height,gender) = (None,None)
def std_weight(height,gender) :
    if gender == "남자":
        weight = round(height*height*22*0.0001,2)
    elif gender == "여자":
        weight = round(height*height*21*0.0001,2)
    print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
    return height,gender
height,gender = std_weight(175,"여자")