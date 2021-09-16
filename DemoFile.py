# DemoFile.py

#텍스트파일에 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("한글데이터\nabcd\n1234\n")
#읽기나 쓰기 작업을 종료해 달라~~
f.close()

#텍스트파일을 읽기
f = open("c:\\work\\demo.txt", "rt")
#하나의 문자열변수에 몽땅 읽어서 리턴
result = f.read()
print(result)
#어디쯤 읽고 있어?
print( f.tell() )
#처음으로 돌아가(Reset)
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )
#다시 처음으로 돌아가서 리스트로 리턴
f.seek(0)
lst = f.readlines()
print( lst )
f.close()
