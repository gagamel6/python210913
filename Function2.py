# Function2.py
x = 1
#함수 정의
def func(a):
    return x+a

#호출
print(func(1))

#함수 정의
def func2(a):
    x = 2
    return x+a

#호출
print(func2(1))

#불변형식을 함수 내부에서 읽기+쓰기
g = 1
def testScope(a):
    #global g
    #별도의 지역변수로 사용
    g = 2
    return g+a

#함수호출
print(testScope(1))
print("전역변수:", g)

#기본값이 있는 경우(default value)
def times(a=10,b=10):
    return a*b

#호출
print(times())
print(times(5))
print(times(b=6))
print(times(5,6))

#키워드 인자방식으로 전달(파라메터, 매개변수를 상세하게 기술)
def connectURL(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURL("credu.com", "80"))
print(connectURL(port="8080", server="credu.com"))

#가변인자(입력 파라메터 갯수가 가변적)
#고객(갑)  <----------->  개발자(을)
#단어를 2, 3, 10개를 유니크한 문자를 리턴
def union(*ar):
    #지역변수
    result = []
    #HAM(0) | SPAM(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #아직 지역변수에 없으면 추가
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))
