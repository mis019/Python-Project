import sys

option = sys.argv[1]

if option == "-a":   
    memo = sys.argv[2]
    file = open("memo.txt", "a", encoding="utf-8")
    file.write(memo)
    file.write("\n")
    file.close()
elif option == "-v":   
    file = open("memo.txt", encoding="utf-8")
    memo = file.read()
    file.close()
    print(memo)
# print(option)
# print(memo)

