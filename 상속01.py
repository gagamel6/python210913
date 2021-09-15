#부모 클래스를 정의(공통단 정의)
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스를 정의
class Student(Person):
    #학생은 추가로 학번, 학과(상속받아서 재정의, 덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모클래스의 생성자 호출
        #super키워드, base키워드를 제공 자기자신(self)
        #self.name = name
        #self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, Subject:{2}, StudentID:{3})".format(
            self.name, self.phoneNumber, self.subject, self.studentID))

#인스턴스를 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

