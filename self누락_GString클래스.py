#전역변수를 초기화
str = "Not Class Member"

class GString:
    #초기화 메서드
    def __init__(self):
        #인스턴스의 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #모호한 것(str)보다는 명확(self.str)하게 코딩해야 한다(명시~~)
        #print(str) --> print(self.str)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
