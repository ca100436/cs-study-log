# Quiz 1 코드
'''
class Student :
    def __init__(self, name=None, age=0) :
        self.__name = name
        self.__age = age

    def getAge(self) :
        return self.__age

    def getName(self) :
        return self.__name

    def setAge(self, age) :
        if age < 0 :
            self.__age = 0
            print(f"age에 음수 {age}이 입력되었습니다. 기본값 0으로 설정합니다.")
            print("age를 다시 설정해주시기 바랍니다.")
        else :
            self.__age = age
            print(f"age가 입력하신 {age}로 설정되었습니다.")

    def setName(self, name) :
        self.__name = name

a = Student()
print("Name의 초기값은", a.getName())
print("Age의 초기값은", a.getAge())

a.setAge(-10)
a.setAge(20)
'''
# Quiz 2 코드
'''
class BankAccount :
    def __init__(self, balance=0) :
        self.balance = balance

    def deposit(self, money) :
        self.balance += money
        print(f"통장에 {money}원 입금되었음,")
        print(f"현재 잔액은 {self.balance}원 입니다.")

    def withdraw(self, money) :
        self.balance -= money
        print(f"통장에서 {money}원 출금되었음.")
        print(f"현재 잔액은 {self.balance}원 입니다.")

a = BankAccount()
a.deposit(100)
a.withdraw(10)
'''
# Quiz 3 코드
'''
class BankAccount :
    def __init__(self, name=None, balance=0) :
        self.name = name
        self.balance = balance

        print(f"{self.name}님 환영합니다.")
        print(f"초기 금액 {self.balance}원으로 계좌가 만들어졌습니다.")

    def deposit(self, money) :
        self.balance += money
        print(f"통장에 {money}원 입금되었음.")
        print(f"현재 잔액은 {self.balance}원 입니다.")

    def withdraw(self, money) :
        self.balance -= money
        print(f"통장에서 {money}원 출금되었음.")
        print(f"현재 잔액은 {self.balance}원 입니다.")

a = BankAccount()
b = BankAccount("눈송이", 100)
'''
# Quiz 4 코드
'''
class BankAccount :
    def __init__(self, name=None, balance=0) :
        self.name = name
        self.balance = balance

        print(f"{self.name}님 환영합니다.")
        print(f"초기 금액 {self.balance}원으로 계좌가 만들어졌습니다.")

    def deposit(self, money) :
        self.balance += money
        print(f"통장에 {money}원 입금되었음.")
        print(f"현재 잔액은 {self.balance}원 입니다.")

    def withdraw(self, money) :
        if money > self.balance :
            print("출금하려는 금액이 현재 잔액보다 큽니다.")
            print("출금이 이루어지지 않습니다.")
            print(f"현재 잔액은 {self.balance}원 입니다.")
        else :
            self.balance -= money
            print(f"통장에서 {money}원 출금되었음.")
            print(f"현재 잔액은 {self.balance}원 입니다.")

a = BankAccount()
a.deposit(100)
a.withdraw(200)
a.withdraw(50)

b = BankAccount("눈송이", 100)
'''
# Circle 클래스 (원 넓이 + 둘레)
'''
import math

class Circle :
    def __init__(self, radius) :
        self.radius = radius

    def getArea(self) :
        return math.pi * self.radius ** 2

    def getPerimeter(self) :
        return 2 * math.pi * self.radius

c = Circle(10)

print("원의 면적 : ", c.getArea())
print("원의 둘레 : ", c.getPerimeter())
'''
# FourCal 생성자 추가
'''
class FourCal :
    def __init__(self, first, second) :
        self.first = first
        self.second = second

    def sum(self) :
        return self.first + self.second

    def sub(self) :
        return self.first - self.second

    def mul(self) :
        return self.first * self.second

    def div(self) :
        return self.first / self.second

a = FourCal(4, 2)

print(a.first)
print(a.second)
print(a.sum())
print(a.div())
'''
