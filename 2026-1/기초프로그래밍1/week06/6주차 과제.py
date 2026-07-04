# 과제 1 : 가고자 하는 층수를 입력했을 때 현재 층에서부터 가는 층수 출력하기
'''
now = 5
floor = int(input("가는 층수를 입력해주세요(1~10층) : "))
print("현재", now, "층입니다.")

if floor > now :
    for i in range (now + 1, floor + 1) :
        print(i, "층입니다.")
elif floor < now :
    for i in range (now - 1, floor - 1, -1) :
        print(i, "층입니다.")
else :
    print("이미 현재 층입니다.")
'''
# 과제 2 : 랜덤 현재 층 + 입력받은 층까지 이동하기
'''
import random

now = random.randint(1, 10)
floor = int(input("가는 층수를 입력하세요(1~10층) : "))
print("floor =", floor, "now =", now)

if floor < 1 or floor > 10 :
    print("오류! 1~10층 사이만 입력하세요.")
else :
    if now < floor :
        for i in range (now, floor + 1) :
            print("현재 층은", i, "층입니다.")
    elif now > floor :
        for i in range (floor, now - 1, -1) :
            print("현재 층은", i, "층입니다.")
    else :
        print("현재 층은", now, "층입니다.")

    print("도착하였습니다. 안녕히 가십시오!")
'''
# 과제 3 : 주사위 2개 던졌을 때 합이 6이 되는 경우 모두 출력하기
'''
for i in range(1, 6) :
    print("첫번째 주사위 = ", i, "두번째 주사위 = ", 6 - i)
'''
# 과제 4 : 1부터 10까지에서의 3의 배수만 빼고 출력하기
'''
for i in range(1, 11) :
    if i % 3 != 0 :
        print(i, end = ' ')
'''
# 과제 5-1 : hello 함수
'''
def hello() :
    print("안녕 파이썬")
    print("즐거운 코딩시간이야")
hello()
'''
# 과제 5-2 : goodbye 함수
'''
def goodbye() :
    print("파이썬 어렵지않아")
    print("다음 시간에 또 만나요")
goodbye()
'''
# 과제 5-3 : how_old_are_you 함수
'''
def how_old_are_you(year) :
    print(year, "년생 : 올해 22살입니다")
how_old_are_you(1988)
'''
# 과제 6-1 : 정수를 입력받아서 제곱값 반환하는 함수
'''
def square(num) :
    return num * num
n = int(input("정수를 입력하세요 : "))
print(square(n))
'''
# 과제 6-2 : 두 정수 중 더 큰 수를 반환하는 함수
'''
def bigger(a, b) :
    if a > b :
        return a
    else :
        return b
num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))
print(bigger(num1, num2))
'''
# 과제 6-3 : 입력받은 수가 짝수인지 홀수인지 출력하는 함수
'''
def old_even(num) :
    if num % 2 == 0 :
        print("짝수입니다")
    else :
        print("홀수입니다")
n = int(input("정수를 입력하세요 : "))
old_even(n)
'''
# 과제 6-4 : 정수의 거듭제곱 값을 반환하는 함수
'''
def power(a, b) :
    result = 1
    for i in range(b) :
        result *= a
    return result
num = int(input("밑을 입력하세요 : "))
exp = int(input("지수를 입력하세요 : "))
print(power(num, exp))
'''
# 과제 6-5 : 입력으로 들어오는 모든 수의 평균값 계산 함수
'''
def avg(*numbers) :
    return sum(numbers) / len(numbers)
print(avg(10, 20, 30))
print(avg(1, 2, 3, 4, 5))
'''
# 과제 7 : lambda로 2개 정수 (100, 200)를 크기 순으로 변환하기
'''
f = lambda a, b : (a , b) if a < b else (b , a)
print(f(100, 200))
'''