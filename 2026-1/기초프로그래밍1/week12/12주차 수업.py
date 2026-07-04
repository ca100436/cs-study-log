# try_except.py
'''
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
'''
# try_finally 1.py
'''
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행
except ZeroDivisionError as e:
    print(e)
finally:
    f.close()
'''
# try_finally 2.py
'''
try:
    print('예외가 있을때')
    number = 4 / 0
    print('다음 코드들...')
except:
    print('except블록')
else:
    print(' else블록 ')
finally:
    print(' finally블록 ')
print('************')
try:
    print('예외가 없을때')
    number = 4 / 4
    print('다음 코드들...')
except:
    print('except블록')
else:
    print('else블록')
finally:
    print('finally블록')
'''
# error_pass.py
'''
try:
    f = open("나없는파일",'r')
except FileNotFoundError:
    pass
'''
# raise.py
'''
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
'''
#error2.py
'''
class MyError(Exception):
    def __str__(self):
        return 'This is my error'
try:
    raise MyError
except Exception as e:
    print(e)
'''
# error_raise.py
'''
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
'''
# error_make.py
'''
class MyError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
'''
# 내장 함수

print(abs(3))
print(abs(-3))
print(abs(-1.2))

print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))

print(any([1, 2, 3, 0]))
print(any([0, ""]))
print(any([]))

print(chr(97))
print(chr(44032))

print(dir([1, 2, 3]))
print(dir({'1':'a'}))

print(divmod(7, 3))
print(7 // 3)
print(7 % 3)

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(hex(234))
print(hex(3))

a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))
'''
a = input()
print(a)
b = input("Enter: ")
print(b)
'''
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))

class Person: pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))