'''
작성일 : 2023년 3월 28일
학과 : 
학번 : 
이름 : 
설명 : 변수 사용법과 자료형 알아보기
        print()함수 사용법 익히기.
'''
#변수 num1에 10을 배정하시오.
num1 = 10
# 변수 num2에 20을 저장하시오.
num2 = 20 #첫 칸 띄어쓰기 하지 말 것!!!

# 변수에 3.14를 저장하시오
pi = 3.14

# 변수에 자기 이름을 저장하시오
name = "임수현"

#num1, num2에 저장된 값을 더하여 total에 저장

total = num1 + num2
print("num1 변수에 저장된 값 : ",num1)
print("num2 변수에 저장된 값 : ",num2)

print("pi변수에 저장된 값은 {}입니다".format(pi))

print("나의 이름은",name,"입니다.")
print("나의 이름은 {}입니다".format(name))

print(num1,"+",num1,"=",total)
print("{} + {} + {}" .format(num1,num2,total))

# 변수의 자료형을 알아보기 위해 쓰는 함수
# type()
print("num1의 자료형 : ",type(num1))
print("pi의 자료형 : ",type(pi))
print("name의 자료형 : ",type(name))