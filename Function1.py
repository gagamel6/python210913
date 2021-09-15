# Function1.py
#리턴을 하지 않는 경우
def setValue(newValue):
    #함수 내부에서 초기화(지역변수)
    x = newValue
    print("함수 내부:", x)

#함수 호출
result = setValue(5)
print(result)

#리턴을 하는 경우(Tuple형식)
def swap(x,y):
    return y,x

#호출
result = swap(5,6)
print(*result)

#디버깅을 연습하기 위한 데모
def intersect(prelist, postlist):
    #교집합 문자를 리턴하는 함수
    #함수 내부에 교집합 문자를 모아두기
    result = []
    #H[0] A[1] M[2]
    for x in prelist:
        #만약 postlist에 글자가 있고 그리고 result에 아직 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result

#함수 호출
print(intersect("HAM","SPAM"))

#불변형식
print("---불변형식---")
a = 1.2
print(id(a))
a = 2.3
print(id(a))

#가변형식
print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#참조형식을 입력 데이터로 사용해도 입출력이 된다~~
wordlist = ["J", "A", "M"]
def change(x):
    #함수내부에서 복사본을 생성(깊은 복사, Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

#함수 호출(Pass By Reference)
change(wordlist)
print("함수 호출후:", wordlist)
