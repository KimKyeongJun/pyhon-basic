# gun = 10

# def  checkpoint(soldiers): # 경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))
# # 실행안됨! gun이 지역 변수

gun = 10

def  checkpoint(soldiers): # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

