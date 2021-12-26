from random import *


cnt = 0
for customer in range(1, 51):
    print(customer)
    time = randrange(5,51) # 5 ~ 50분 소요시간
    if 5 <= time <=15: # 매칭 성공5~15분 이내 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        cnt += 1
    else: #매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("총 탑승 승랙 : {0}명".format(cnt))