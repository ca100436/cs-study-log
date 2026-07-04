# 정수 리스트 만드는 함수 : range
'''
number_list = range(10)
print(number_list)
print(list(number_list))
'''
# if문의 기본구조
'''
money = 1
if money :
    print("택시를 타고 가라")
else :
    print("걸어가라")
'''
# 조건문 (비교연산자)
'''
x = 3
y = 2

print(x > y)

print(x < y)

print(x == y)

print(x != y)
'''
# 조건문 (비교연산자)
'''
money = 2000
if (money >= 3000) :
    print("택시를 타고 가라")
else :
    print("걸어 가라")
'''
# 조건문 (and, or, not)
'''
money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else :
    print("같이 타라")
'''
# 조건문 (x in s, x not in s(in 연산자))
'''
print(1 in [1,2,3])
print(1 not in [1,2,3,])
'''
# elif (if-else만으로 구현)
'''
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    if card :
        print("택시를 타고 가라")
    else :
        print("걸어 가라")
'''
'''
treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10 :
        print("나무 넘어갑니다.")
'''
# while문 만들기
'''
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4 :
    print(prompt)
    number = int(input())
'''
# while문 강제로 빠져나가기
'''
# coffee.py
coffee = 3
money = 300
while money :
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d입니다." % coffee)
    if not coffee :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''
'''
# coffee.py
coffee = 3
while True :
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300 :
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300 :
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else :
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    print("남은 커피의 양은 %d잔입니다." % coffee)
    if not coffee :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''
# while문의 맨 처음으로 돌아가기 (continue 문)
'''
a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0 : continue
    print(a)
'''
while True :
    print("Ctrl+C를 늘려야 while문을 빠져나갈 수 있습니다.")
'''