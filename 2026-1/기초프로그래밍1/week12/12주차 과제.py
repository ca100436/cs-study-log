# Quiz.1
'''
while True:
    try:
        num = int(input("숫자를 입력하세요 : "))
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하세요.")

print("정수 입력이 성공하였습니다!")
'''

# Quiz.2
'''
class AccountBalanceException(Exception):
    pass
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        print(f"{self.name} 님 환영합니다.")
        print(f"초기 금액 {self.balance} 으로 계좌가 만들어졌습니다.")

    def withdraw(self, money):
        try:
            if money > self.balance:
                raise AccountBalanceException

            self.balance -= money
            print(f"{money}원 출금되었습니다.")

        except AccountBalanceException:
            print("Account Balance Exception Occurs : Check your balance")

        finally:
            print(f"현재 잔액은 {self.balance} 입니다.")

a = BankAccount("홍길동", 100)
a.withdraw(200)
'''
# Quiz.3
'''
class AccountBalanceException(Exception):
    pass

class InvalidTransactionException(Exception):
    pass

class BackAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        print(f"{self.name} 님 환영합니다.")
        print(f"초기 금액 {self.balance} 으로 계좌가 만들어졌습니다.")

    def withdraw(self, money):
        try:
            if money > self.balance:
                raise AccountBalanceException

            self.balance -= money
            print(f"{money}원 출금되었습니다.")

        except AccountBalanceException:
            print("Account Balance Exception Occurs : Check your balance")

        finally:
            print(f"현재 잔액은 {self.balance} 입니다.")

    def deposit(self, money):
        try:
            if money < 0:
                raise InvalidTransactionException

            self.balance += money
            print(f"{money}원 입금되었습니다.")

        except InvalidTransactionException:
            print("Invalid Transaction Exception Occurs : Check your account")

        finally:
            print(f"현재 잔액은 {self.balance} 입니다.")
            
a = BankAccount("홍길동", 100)
a.withdraw(-100)
'''