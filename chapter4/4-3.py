# file = open("chapter4/fileTest.txt","w", encoding="utf-8")
# file.write("파일생성 테스트""\n")
# file.write("파일생성 테스트22""\n")
# file.close()

# file = open("E:/Python Project/chapter4/fileTest.txt","r", encoding="utf-8")
# while file:
#     line = file.readline()
#     if not line:
#         break
#     print(line.strip())

# file.close()

# file = open("E:/Python Project/chapter4/fileTest.txt","r", encoding="utf-8")
# data = file.read()
# print(data)
# file.close()

file = open("chapter4/fileTest.txt","a", encoding="utf-8")
file.write("파일내용 추가 테스트""\n")
file.write("파일내용 추가 테스트22""\n")
file.close()