# DemoLoop.py
# Outer for in 루프
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    # Inner for in 루프
    for y in [1,2,3,4,5,6,7,8,9,10]:
        print("{0} * {1} = {2}".format(x, y, x*y))

#삼각형
for i in [1,2,3,4,5,6,7,8,9]:
    print("*" * i)

print("---break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열 함수 연습
print(range(10))
print(list(range(10)))
print(list(range(1,11)))
print(list(range(10,0,-1)))
print(list(range(2000,2022)))

print("---리스트 내장 형식---")
#반복구문을 실행하면서 필터링을 하고 가공까지 한줄에 코딩
#파이썬스럽다~~
lst = [1,2,3,4,5,6,7,8,9,10]
print([i**2 for i in lst if i > 5])

tp = ("apple", "kiwi")
print([len(i) for i in tp])

d = {100:"apple", 200:"banana", 300:"kiwi"}
print([v.upper() for v in d.values()])

#반복문에서 필터링하는 함수
def getBiggerThan20(i):
    return i > 20

lst = [10,25,30]
print(lst)
#함수를 호출
iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print(i)

