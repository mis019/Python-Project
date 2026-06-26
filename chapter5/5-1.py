result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print("def1 : "+str(add1(3)))
print("def1 : "+str(add1(4)))

print("def2 : "+str(add2(5)))
print("def2 : "+str(add2(6)))