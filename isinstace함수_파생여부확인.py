#무조건 부모가 object클래스 (class Person(object)와 같다)
class Person:
    pass

class Bird:
    pass

#부모 클래스인 Person은 상속받은 자식 클래스 정의
class Student(Person):
    pass

#다른 언어들은
#Person p = new Person()
#Student s = new Student()
p, s = Person(), Student()
#isinstance()함수는 특정 형식의 인스턴스 여부? True, False
#~.print() 메서드  |  isinstance() 함수
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))
