# for문의 기본구조 (for문의 예)
'''
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)
'''
from ctypes import HRESULT

# for문의 기본구조 (다양한 for문의 사용)
'''
a = [(1,2),(3,4),(5,6)]
for (first, last) in a :
    print(first+last)
'''
# Quiz 1_whileStar.py [별(*)을 표시하는 프로그램]
'''
i = 0
while True :

    i += 1             # while문 수행 시 1씩 증가
    if i > 5 : break
    print("*" * i)
        # i가 5보다 크면 while문을 벗어남
'''
# Quiz 2_whileStar.py [별(*)을 표시하는 프로그램]
'''
j = 6
for i in (1,2,3,4,5) :
    print(" " * j, "*" * i)
    j -= 1
'''
# Marks1.py [for문의 기본구조 (for문의 응용)]
'''
marks = [90, 25, 67, 45, 80]
number = 0              # 학생에게 붙여줄 번호
for mark in marks :     # marks 요소를 순서대로 mark에 대입
    number += 1
    if mark >= 60 :
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)
'''
# Marks2.py [for문과 continue]
'''
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number += 1
    if mark < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
'''
# for문과 함께 자주 사용하는 range 함수 1
'''
for i in range(100) :
    print("Hello, world!")
'''
# for문과 함께 자주 사용하는 range 함수 2-1
'''
a = range(10)
print(a)
print(type(a))
'''
# for문과 함께 자주 사용하는 range 함수 2-2
'''
a = range(1,11)
print(a)
print(list(a))
'''
# for문과 함께 자주 사용하는 range 함수 3 (감소하기)
'''
for i in range(10, 0, -2) :
    print("Hello, world!", i)
'''
# for문과 함께 자주 사용하는 range 함수 3 (감소하기)
# 60점 이상이면 합격을 출력하는 예시를 range로 구현하기
'''
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)) :
    if marks[number] < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
'''
# for문과 함께 자주 사용하는 range 함수 3 (감소하기)
# for와 range를 이용한 구구단
'''
for i in range(2,10) :
    for j in range(1,10) :
        print(i*j, end=" ")
    print('')
'''
# Quiz 구구단 2~9단까지 출력하기 (방법 1)
'''
for i in range(2,10) :
    print("구구단", i, "단시작!", end=" ")
    for j in range(1,10) :
        print(i*j, end=" ")
    print('')
'''
# GUGUDAN 1
'''
j = int(input("단을 입력하세요.(2~9단) : "))
for i in range(1, 10) :
    print(j,"*",i,"= ",j*i)
'''
# GUGUDAN 2
'''
i = input("단을 입력하세요.(2~9단) : "))
for i in range(1, 10) :
    print(j,"*",i,"= ",j*i)
'''
# 리스트 내포 사용하기 1
'''
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)
'''
# 리스트 내포 사용하기 2
'''
a = [1,2,3,4]
result = []
result = [num*3 for num in a]
print(result)
'''
# 리스트 내포 사용하기 3
# 짝수에만 3을 곱하기
'''
a = [1,2,3,4]
result = []
result = [num*3 for num in a if num % 2 == 0]
print(result)
'''
# 리스트 내포 사용하기 3
# 구구단의 결과를 모두 리스트에 담기
'''
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)
'''
# random 함수 (주사위 문제)
'''
import random
print(random.randrange(1,7))
print(random.randrange(1,7))
'''
# Star.py
'''
import turtle
t = turtle.Turtle()
colors = ["Red", "Yellow", "Green"]
for i in range(3) :
    t.begin_fill()
    t.fillcolor(colors[i])
    for j in range(5) :
        t.forward(100)
        t.left(144)
    t.end_fill()
    t.left(120)
turtle.done()
'''
# range()에서 step 저장하기
'''
print([n/10 for n in range(1,11)])
'''
# 입력값이 몇 개가 될지 모를 때
# 여러 개의 입력 값을 받는 함수 만들기
'''
def add_many(*args) :
    result = 0
    for i in args :
              result += i
    return result
print(add_many(1,2))
print(add_many(1,2,3))
print(add_many(1,2,3,4,5))
'''
# 입력값이 몇 개가 될지 모를 때
# 키워드 파라미터
'''
def print_kwargs(**kwargs) :
    print(kwargs)
print(print_kwargs(a=1))
print(print_kwargs(name='foo', age=3))
'''
# 함수의 결과값은 언제나 하나이며 return의 또 다른 쓰임새
'''
def say_nick(nick) :
    if nick == '바보' :
        return
    print("나의 별명은 %s입니다." % nick)
'''
# 매개변수에 초기값 미리 설정하기
'''
def say_myself(name, age, sju_stdent = True) :
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d 살입니다." % age)
    if sju_stdent :
        print("상지대 학생입니다.")
    else :
        print("상지대 학생이 아닙니다.")
say_myself("홍길동, 20"))
'''
# lambda
'''
print(lambda a,b : a+b) (10, 20)
'''
