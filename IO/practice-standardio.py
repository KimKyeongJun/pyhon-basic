print("Python", "Java", sep=",")
print("Python", "Java", "Javascript", sep=" vs ")

print("Python", "Java", "Javascript", sep=",", end="?")
print("무엇이 더 재밌을까요?")


import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러


scores = {"수학" : 0, "영어":50, "코딩":100}
for subject, score in  scores.items():
    #print(subject, score)
    # 8개 공간을 만들고 왼쪽 정렬
    # 4개 공간을 만들고 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21):
     print("대기번호 : " + str(num).zfill(3))


# input 함수에 타입을 지정하지 않으면 항상 string으로 간주한다.
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 : {0} 입니다.".format(answer))