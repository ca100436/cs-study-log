# 절자지향프로그램 1
'''
showinfo = " "
def Person(name, age) :
    showinfo = "이름 : " + name + ", " + "나이 : " + age
    return showinfo

print(Person("홍길동", "27"))
'''
# 절자지향프로그램 2
'''
showinfo = " "
def Person(name, age) :
    global showinfo
    showinfo = "이름 : " + name + ", " + "나이 : " + age + "\n"
    return showinfo

print(Person("홍길동", "27"))
print(Person("홍길순", "18"))

print(showinfo)
'''
# 절자지향프로그램 3
'''
w_showinfo = " "
m_showinfo = " "
def M_Person(name, age) :
    global m_showinfo
    m_showinfo += "이름 : " + name + ", " + "나이 : "+ age + "\n"

def W_Person(name, age) :
    global w_showinfo
    w_showinfo += "이름 : " + name + ", " + "나이 : "+ age + "\n"

M_Person("홍길동", "27")
W_Person("허초희", "29")
W_Person("홍길순", "25")
M_Person("허  균", "24")

print(m_showinfo)
print(w_showinfo)
'''
# 객체지향프로그램
'''
class Person :

    def __init__(self) :
           self.info = " "

    def showinfo(self, name, age) :
           self.info += "이름 : " + name + ", 나이 :" + age + "\n"
           print(self.info)

man = Person()
woman = Person()

man.showinfo("홍길동", "27")
woman.showinfo("홍길순", "25")
woman.showinfo("허초희", "29")
'''
# 클래스는 왜 필요한가?
'''
class Calculator :
    def __init__(self) :
        self.result = 0
        
    def adder(self, num) :
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
'''
# 이야기 형식으로 클래스 기초 쌓기
'''
class Service :
    secret = '임금님 귀는 당나귀 귀.'
    def setname(self, name) :
       self.name = name
    def sum(self, a, b) :
       result = a + b
       print("%s님, %s + %s = %s 입니다" % (self.name, a, b, result))

pey = Service()
pey.setname('홍길동')
pey.sum(1,1)
'''
# 객체에 숫자 지정할 수 있게 만들기
'''
# 1번 문제 (print(a.first)와 print(a.second)를 실행하여 입력한 대로 각각 설정하기
class FourCal :
    def setdata (self, first, second) :
        self.first = first
        self.second = second
# 2번 문제 (b라는 객체를 하나 더 만들어 새로운 값 3과 7 설정하기)
a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
b = FourCal()
b.setdata(3,7)
print(b.first)
print(b.second)
# 3번 문제 (a와 b의 first가 각각 다른 값인지 직접 확인)
print(a.first)
print(b.first)
'''
# 사칙연산 클래스 만들기
'''
class FourCal :
    def setdata (self, first, second) :
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)

b = FourCal()
b.setdata(3,7)
print(b.first)
print(b.second)

print(a.first)
print(b.first)
'''
# 더하기 기능 만들기
'''
# a.sum()을 수행하면 두 값을 더하도록 클래스 함수 추가하기
class FourCal :
        def setdata (self, first, second) :
                self.first = first
                self.second = second
        def sum(self) :
                result = self.first + self.second
                return result
# print(a.sum())을 실행하여 돌려주는 값 확인하기
a = FourCal()
a.setdata(4,2)
print(a.sum())
'''
# __init__(생성자) 활용법
'''
class Television :
    def __init__(self, channel = 99, vol = 3, on = 'True') :
        self.channel = channel
        self.vol = vol
        self.on = on

    def show(self) :
        print(self.channel, self.vol, self.on)

    def setChannel(self, channel) :
        self.channel = channel

    def setVolume(self, vol) :
        self.vol = vol
t = Television()
t.show()

t.setChannel(30)
t.show()
'''
# 접근자와 설정자
'''
class Student :
    def __init__(self, name, age) :
        self.__name = name
        self.__age = age
    def getAge(self) :
        return self.__age
    def getName(self) :
        return self.__name
    def setAge(self, age) :
      if age < 0 :
          self.__age = 0
      else :
          self.__age = age
    def setName(self, name) :
      self.__name = name
a = Student("Hong", 20)
a.setAge(-10)
print(a.getAge())
'''