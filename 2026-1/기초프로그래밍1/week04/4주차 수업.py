# 두 단어로 구성된 문자열에서 단어의 순서룰 바꾸고 단어의 문자를 역순시키기
'''
str = input("2개의 단어를 빈공간으로 구분해 입력해보세요.>>")
pos = str.find(' ')
preword = str[:pos]
postword = str[pos+1:]
print(preword, postword)
print(preword[::-1], postword[::-1])
'''
# 리스트의 인덱싱
'''
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0]+a[2])
'''
# 리스트의 인덱싱 2
'''
b = [1,2,3,['a','b','c']]
print(b[0])
print(b[-1])
print(b[3])
print(b[3][0])
'''
# 리스트의 인덱싱 3
'''
c = [1,2,3,['a','b','c']]
print(c[3][0])
print(c[-1][0])
'''
# 리스트의 인덱싱 4 (삼중 리스트)
'''
d = [1,2,['a','b',['Life','is']]]
print(d[2][-1][0])
print(d[2][2][0])
print(d[-1][2][0])
'''
# 리스트의 슬라이싱 <리스트>
'''
a = [1,2,3,4,5]
print(a[0:2])
'''
# 리스트의 슬라이싱 <문자열>
'''
a = "12345"
print(a[0:2])
'''
# 리스트의 슬라이싱 (중첩된 리스트)
'''
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])
'''
# 리스트의 더하기(+)
'''
a = [1,2,3]
b = [4,5,6]
print(a+b)
'''
# 리스트의 반복하기(*)
'''
a = [1,2,3]
print(a*3)
'''
# 리스트의 길이구하기
'''
a = [1,2,3]
print(len(a))
'''
# 리스트에서 하나의 값 수정하기
'''
a = [1,2,3]
a[2] = 4
print(a)
'''
# 리스트에서 연속된 범위의 값 수정하기
'''
a = [1,2,3,4]
print(a[3])
a[3] = 5
print(a)
print(a[2:3])
a[2:3] = ['a','b']
print(a)
'''
# 리스트 요소 삭제하기 ([]사용)
'''
a = [1,2,3,4,5,6,7,8,9]
del a[1:5]
print(a)
'''
# del함수 이용
'''
a = [1,2,3,4,5,6,7,8,9]
del a[1:5]
print(a)
'''
# 리스트에 요소 추가 (append)
'''
a = [1,2,3,4,5,6,7,8,9]
a.append(10)
print(a)
'''
# 리스트 뒤집기 (reverse)
'''
a = ['a','c','b']
a.reverse()
print(a)
'''
# 위치반환 (index)
'''
a = [1, 2, 3]
print(a.index(3))
'''
# 리스트에 요소 삽입 (insert)
'''
a = [1,2,3]
a.insert(0,4)
print(a)
a.insert(3,5)
print(a)
'''
# 리스트에 요소 제거 (remove)
'''
a = [1,2,3,1,2,3]
a.remove(3)
print(a)
a.remove(3)
print(a)
'''
# 리스트에 요소 끄집어내기 (pop)
'''
a = [1,2,3]
print(a.pop())
print(a)
b = [1,2,3]
print(b.pop(1))
print(b)
'''
# 리스트에 포함된 요소 x의 개수 세기 (count)
'''
a = [1,2,3,1]
print(a.count(1))
'''
# 리스트 확장 (extend)
'''
a = [1,2,3]
a.extend([4,5])
print(a)
'''
# 튜플 다루기 (인덱싱)
'''
t1 = (1,2,'a','b')
print(t1[0])
print(t1[-1])
'''
# 튜플 다루기 (슬라이싱)
'''
print(t1[1:])
'''
# 튜플더하기
'''
t2 = (3,4)
print(t1+t2)
'''
# 튜플곱하기
'''
t2 = (3,4)
print(t2*3)
'''
# 튜플길이 구하기
'''
t1 = (1,2,3,4)
print(len(t1))
'''
# (1,2,3)이라는 튜플에 값 4를 추가하여 (1,2,3,4) 만들기
'''
t1 = (1,2,3)
print(t1 + (4,))
'''
# 딕셔너리 쌍 추가하기 1
'''
a = {1:'a'}
a[2] = 'b'
print(a)
'''
# 딕셔너리 쌍 추가하기 2
'''
a['name'] = 'pey'
print(a)
'''
# 딕셔너리 쌍 추가하기 3
'''
a[3] = [1,2,3]
print(a)
'''
# Key 이용하여 Value 얻기
'''
grade = {'pey':10, 'julliet':99}
print(grade['pey'])
'''
# Key는 고유한 값
'''
a = {1:'a',1:'b'}
print(a)
'''
# Key리스트 만들기(keys) 1
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
'''
# Key리스트 만들기(keys) 2
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
for k in a.keys() :
    print(k)
'''
# Key리스트 만들기(keys) 3
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(list(a.keys()))
'''
# Value리스트 만들기(values)
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
grade = {'pey':10, 'julliet':99}
print(a.values())
'''
# Key, Value 쌍 얻기 (items)
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.items())
'''
# Key, Value 쌍 모두 지우기 (clear)
'''
print(a)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.clear())
print(a)
'''
# Key로 Value얻기(get) 1
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name'))
print(a['name'])
'''
# Key로 Value얻기(get) 2
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('nokey'))
'''
# Key로 Value얻기(get) 3
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('foo','bar'))
'''
# 해당 Key가 딕셔너리안에 있는지 조사하기(in)
'''
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a)
print('email' in a)
'''
# 집합 : set 키워드를 이용하여 만들기 (리스트)
'''
s1 = set([1,2,3])
print(s1)
'''
# 집합 : set 키워드를 이용하여 만들기 (문자열)
'''
s2 = set("Hello")
print(s2)
'''
# 집합 : Set 형은 인덱싱 지원 X
'''
s1 = set([1,2,3])
print(s1)
'''
# 집합 : List 형은 인덱싱 지원 O
'''
L1 = [1,2,3]
print(L1)
'''
# 집합 예제 1-1 [교집합(& 기호, intersection 함수사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
'''
# 집합 예제 1-2 [교집합(& 기호, intersection 함수사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2))
'''
# 집합 예제 1-3 [교집합(& 기호, intersection 함수사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s2.intersection(s1))
'''
# 집합 예제 2-1 [합집합(| 기호, union 함수 사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 | s2)
'''
# 집합 예제 2-2 [합집합(| 기호, union 함수 사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.union(s2))
'''
# 집합 예제 2-3 [합집합(| 기호, union 함수 사용)]
'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s2.union(s1))
'''
# 집합 예제 3 [차집합(- 기호, difference 함수 사용)]

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))
print(s2.difference(s1))

# add 함수 : 하나씩 추가할 경우
'''
s1 = set([1,2,3])
s1.add(4)
print(s1)
'''
# update 함수 : 여러 개의 값을 한꺼번에 추가할 경우
'''
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
'''
# 불자료형 예제 : 조건문(if)
# []가 참이라면 "True"를 출력하고, 그렇지 않으면 "False"를 출력하기

if [] :
    print("True")
else :
    print("False")
    
# 불자료형 예제 : 조건문(if)
# [1,2,3]이 참이라면 "True"를 출력하고, 그렇지 않으면 "False"를 출력하기

if [1,2,3] :
    print("True")
else :
    print("False")


