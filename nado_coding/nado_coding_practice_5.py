from multiprocessing.spawn import prepare


class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location =location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year= completion_year
        pass

    # 매물 정보 표시
    def show_detail(self):
        print(f"위치:{self.location} 주택형:{self.house_type} 매매:{self.deal_type} 가격:{self.price} 준공연도:{self.completion_year}")
        pass
houses =[]
house1 = House("강남", "아파트", "매매", "10억", "2010년")
houses.append(house1)
print(f"총 {len(houses)}대의 매물")
house1.show_detail()