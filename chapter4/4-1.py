gVar = 0

def testMultipl(a,b):
    print(f"{a}곱하기 {b}는 {a*b}입니다.")
    global gVar
    gVar = a*b

noReturn = testMultipl(4,9)
print(gVar)