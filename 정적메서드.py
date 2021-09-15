# 정적메서드.py
class MyCalc(object):
    #클래스에서 직접 호출하는 메서드(정적, 클래스 메서드)
    #데코레이터:마크, 표식
    @staticmethod
    def my_add(x,y):
        return x+y

##인스턴스를 생성
#calc = MyCalc

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

