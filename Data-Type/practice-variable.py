animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True\n")


## String을 +로 붙이면 str 함수 호출이 필요하고 ,로 붙이면 str 함수 호출을 할 필요 없다
print("우리집 " , animal , "의 이름은 " , name ,"예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))