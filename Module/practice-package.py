# 패키지 : 모듈들을 모아놓은 집합
import travel.thailand # class나 함수는 직접 import 할 수 없다

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()