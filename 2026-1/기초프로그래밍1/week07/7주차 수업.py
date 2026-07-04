# 파일 생성하기

f = open("새파일.txt", 'w')
f.close()

# 파일을 쓰기 모드로 열어서 출력값 적기 1

for i in range(1, 11) :
    data = "%d 번째 줄입니다." % i
    print(data)

# 파일을 쓰기 모드로 열어서 출력값 적기 2

f = open("새파일.txt", 'w')
for i in range(1, 11) :
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)

f.close()

# readline()을 이용하는 방법 1

f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# readlines()을 이용하는 방법

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines :
    print(line)
f.close()

# readline()을 이용하는 방법 2

f = open("새파일.txt", 'r')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()

# 외부파일을 읽는 여러가지 방법

f = open("새파일.txt", 'r')
lines = f.readlines()
print(lines)
for lines in lines :
    print(lines)
f.close()

# 외부파일을 읽는 여러가지 방법

f = open("새파일.txt", 'r')
lines = f.readlines()
print(lines)
for lines in lines :
    print(line)
f.close()

# 파일에 새로운 내용 추가하기

f = open("새파일.txt", 'a')
for i in range(11, 20) :
    data = "%d 번째 줄입니다." % i
    f.write(data)
f.close()

# sys모듈 입력
# sys1.py

import sys
args = sys.argv[1:]
for i in args :
    print(i)

# sys2.py

import sys
args = sys.argv[1:]
for i in args :
    print(i.upper(), end = ' ')

# 텍스트 입출력 기법

f = open('phones.txt', 'r')
for line in f :
    print(line)
f.close()

# 텍스트 입출력 기법
f = open('numbers.txt', 'w')
for i in range(10) :
    f.write(str[i] + ' ')
f.close()

# number1.py
num = float(input("정수를 입력하시오 : "))
if num >= 0 :
    if num == 0 :
        print("0입니다")
    else :
        print("양수입니다")
else :
    print("음수입니다")

# for_factorial.py
fact = 1
n = int(input("정수를 입력하시오 : "))

for i in range(1, n + 1) :
    fact *= i;

print(n, "!= ", fact, "입니다.")