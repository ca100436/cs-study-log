# 연습문제 1
'''
class Book:
    title = ''
    pages = 0
    def __init__(self, title = '', pages = 0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book('파이썬', 500)
book2 = Book('파이썬', 600)
total = book1 + book2
print('책의 페이지의 합 = ', total)
'''
# 연습문제 2
'''
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

missy = Cat('missy', 3)
lucky = Cat('lucky', 5)

print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
'''
#mod1.py
'''
import mod1

print(mod1.add(3, 4))
print(mod1.sub(4, 3))

mod1.safe_add('a', 1)
'''
# mod1.py
'''
from mod1 import add
print(add('a', 1))
from mod1 import add, safe_add
print(safe_add('a', 1))

from mod1 import *
print(safe_add('a', 1))
print(add('a', 1))
'''
# mod2.py
import mod2

result = mod2.add(3, 4)
print(result)