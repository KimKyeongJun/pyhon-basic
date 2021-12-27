# Super

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name ,location, self.speed))

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 슈퍼를 쓸 때는 self 정보는 넘기지 않고 사용
        self.location = location



# 다중 상속일 때 super를 사용하면 첫번째 인자 Class를 사용
# 그렇기 때문에 다중 상속은  super가 아닌 클래스 __init__ 함수를 사용해야한다.
class Unit2:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 드랍쉽
dropship = FlyableUnit()