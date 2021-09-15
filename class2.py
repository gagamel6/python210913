# class2.py
#클래스를 정의
class Person:
    #클래스에서 소속된 멤버변수
    num_person = 0
    #생성자 메서드(초기화 담당)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본 생성)
p1 = Person()
p2 = Person()
p3 = Person()

print("인스턴스 갯수:", Person.num_person)

#런타임(코드 실행중)   |  디자인타입(코딩중)
#런타임에 변수를 추가(동적 형식의 언어)
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )
#이번에는 인스턴스에 추가
p1.age = 30
print( p1.age )
#print( p2.age )
