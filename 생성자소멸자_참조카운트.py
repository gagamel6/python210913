# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    #생성자 메서드(가장 먼저 실행되서 초기화 작업)
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    #소멸자 메서드(가장 마지막에 실행되서 정리 작업)
    #유명무실(?)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
#인스턴스의 사용이 끝난 경우
#대부분의 경우 메모리 관리는 자동(파이썬 인터프리터가 처리)
#d_copy = d
#del d_copy 
#del d

print("전체 코드 실행 종료")




