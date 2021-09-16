# DemoSrt.py

names = ["홍길동", "전우치", "박문수"]
for name in names:
    print("안녕하세요 {0}".format(name))
    print("=" * 40)

#str클래스의 메서드들
#print( dir(str) )

strA = "python is powerful"
print( strA.capitalize() )
print( strA.count("p") )
print( strA.count("p",7) )
print( "MBC2580".isalnum() )
print( "MBC2580".isdecimal() )
print( "2580".isdecimal() )
print( "demo.ppt".endswith("ppt") )

#앞뒤에 있는 공백문자 제거
strB = "  span and ham  "
print( strB )
print( strB.strip() )
strC = "<<<  span and ham  >>>"
print( strC )
print( strC.strip("<> ") )
result = strC.strip("<> ")
result = result.replace("span", "spam egg")
print(result)
#문자열을 공백문자 기준으로 리스트로 변경
lst = result.split()
print( lst )
#다시 문자열로 결합
result2 = ":)".join(lst)
print(result2)
