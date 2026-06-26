import re

data = {"kim":"770101-1234567","lee":"780101-1234567","park":"790101-1234567"}

# 패턴을 미리 컴파일하여 붕어빵 틀처럼 만들어 둡니다.
# 뒤의 숫자 7자리를 통째로 *******로 바꿀 것이므로 앞자리 6개와 하이픈만 그룹으로 잡습니다.
jumin_regex = re.compile(r"(\d{6}-)\d{7}")

for name, jumin in data.items():
    # 컴파일된 객체의 .sub() 메서드를 사용합니다.
    masked_jumin = jumin_regex.sub(r"\1*******", jumin)
    
    print(f"{name} : {masked_jumin}")