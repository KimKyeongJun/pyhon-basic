# 사전(key, value) 키의 중복은 허용되지 않음, Java의 Map
cabinet = {3: '유재석', 100: "김태호"}
print(cabinet)
print(cabinet[3])

print(cabinet.get(3))
# print(cabinet.get[5]) Error 발생
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

# 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)

# 추가
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key  출력
print(cabinet.keys())

#Value 출력
print(cabinet.values())

# key, value 쌍으로
print(cabinet.items())

# 데이터 모두 삭제
print(cabinet.clear())