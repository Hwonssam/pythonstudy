'''from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
trip_to = ThailandPackage() # travel.thailand. 는 생략
trip_to.detail()'''

from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage() # 태국
trip_to.detail()

'''import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치'''