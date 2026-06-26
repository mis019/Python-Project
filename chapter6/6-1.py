def gugu(x):
    result = [] 
    i = 1
    while i < 10:
        result.append(x*i)
        i += 1
    return result

dan = input("원하는 구구단의 단을 입력하세요 : ")
result = gugu(int(dan))
print(result)