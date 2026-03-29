# 숫자형 산술 연산자

money = 1600            # 투입한 돈
price = 1000                 # 물건 값

change = money - price      # 잔돈
print('change ', change)

c500 = change // 500         # 500원 개수
change = change % 500

c100 = change // 100        # 100원 개수

print('coin500 ', c500)
print('coin100 ', c100)

# 문자열 자료형

food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says."
print(say)
say = '"Python is very easy." he says.'
print(say)

multiline = "Life is too short\nYou need Python"       # 줄바꿈 \n 삽입
print(multiline)


print(multiline)

# 문자열 연산하기

head = "Python"
tail = "is fun!"
head + tail
print('Python is fun!')

# 문자열 인덱싱과 슬라이싱 1

a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# 문자열 인덱싱과 슬라이싱 2

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)

# 문자열 인덱싱과 슬라이싱 3

a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])
print(weather)

# 문자열 포매팅

print("I eat %d apples." %3)        # 1. 숫자 바로 대입

print("I eat %s apples." %"five")   # 2. 문자열 바로 대입

number = 3
print("I eat %d apples." % number)    # 3. 숫자 값을 나타내는 변수로 대입

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))     # 4. 2개 이상의 값 넣기

print("Error is %d%." % 98)         

print("Error is %d%%." % 98)

print("%10s" % "hi")
print("%-10sjane." % 'hi')

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

# 고굽 문자열 포맷팅 함수_ .format()

print("I eat {0} apples.". format(3))
print("I eat {0} apples.". format("five"))
number = 3
print("I eat {0} apples.". format(number))
number = 10
day = 3
print("I ate {0} apples. so I was sick for {1} days.". format(number, day))
print("I ate {number} apples. I was sick for {day} days.". format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.". format(10, day=3))
print("{0:<10}". format("hi"))
print("{0:>10}". format("hi"))
print("{0:^10}". format("hi"))
print("{0:=^10}". format("hi"))
print("{0:!^10}". format("hi"))
y = 3.42134234
print("{0:0.4f}". format(y))
print("{0:10.4f}". format(y))
print("{{ and }}". format())

# 소문자를 대문자로 / 대문자를 소문자로 바꾸기 (.upper() / .lower())

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())

# 문자 개수 세기 (.count())

a = "hobby"
print(a.count('b'))

# 위치 알려주기1 (.find())

a = "Python is best choice"
print(a.find('b'))
print(a.find('k'))

# 위치 알려주기2 (.index())

a = "Python is best choice"
print(a.index('b'))
print(a.index('k'))

# 문자열 삽입 (.join())

a = ","
print(a.join('abcd'))

# 왼쪽 공백 지우기 (.lstrip())

a = " hi"
print(a.lstrip())

# 오른쪽 공백 지우기 (.rstrip())

a = "hi "
print(a.rstrip())

# 양쪽 공백 지우기 (.strip())

a = " hi "
print(a.strip())

# 문자열 바꾸기 (.replace())

a = "Life is too short"
print(a.replace("Life", "Your leg"))
