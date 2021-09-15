# DemoTuple.py

tp = (1,2,3)
print( len(tp) )
print( tp[0] )
print( tp[1] )

#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
#디버깅할 때 중지점(Break Point)
result = calc(5,6)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

#형식을 변환할 때
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
print(b)
b.append(4)
c = tuple(b)
print(c)
print(type(c))
