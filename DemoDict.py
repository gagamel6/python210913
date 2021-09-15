#DemoDict.py
color = {"apple":"red", "banana":"yellow"}
print(len(color))
print(color["apple"])
#입력하는 작업
color["cherry"] = "red"
print(color)
#삭제
del color["apple"]
print(color)

#디바이스를 관리(키와 값 맵핑)
device = {"아이폰":5, "아이패드":10, "윈도우":20}
device["맥프레"] = 15
print(device)
device["아이폰"] = 6
del device["아이패드"]
print(device)

#전화번호를 딕셔너리로 관리
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
#반복 구문
#튜플로 받기
for item in phone.items():
    print(item)
#별도의 반복 변수로 받기
for k,v in phone.items():
    print(k,v)
#키만 받는 경우
for k in phone.keys():
    print(k)
#값만 받은 경우
for v in phone.values():
    print(v)

#참조만 복사해서 전달(Pass By Reference, Call By Reference)
p = phone
print(phone)
print(p)
print(id(phone), id(p))
p["moon"] = "1234"
print(phone)
print(p)

print("kang" in phone)
print("kang" not in phone)

print("---논리식---")
print(1<2)
print(1!=2)
print(1==2)
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("demo"))
print(bool([]))
print(bool([1,2,3]))
print(True and True and False)
print(True and True and True)
print(True or False or False)

print("---얕은복사(shallow copy)---")
a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

print("---깊은복사(deep copy)---")
a = [1,2,3]
b = a[:]
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

#리스트형식이 아닌 경우
import copy
a = [100, 200, 300]
b = copy.deepcopy(a)
a[0] = 101
print("a = ", a)
print("b = ", b)
print(id(a), id(b))
