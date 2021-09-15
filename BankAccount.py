# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #멤버 변수도 파이썬에서는 public이다~~
        #인스턴스 멥버 변수 초기화~~
        #클래스 내부에 숨겨달라: __변수명
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#print(account1.__balance)
#외부에서는 접근하기 힘든 변경된 이름이 제공(백도어)
print(account1._BankAccount__balance)

