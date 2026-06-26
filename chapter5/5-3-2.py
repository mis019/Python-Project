def get_josa_eun_neun(word):
    """단어의 마지막 글자에 받침이 있으면 '은', 없으면 '는'을 반환합니다."""
    if not word:
        return "은/는"
    
    # 마지막 글자의 유니코드 값을 가져옵니다.
    last_char = word[-1]
    last_char_code = ord(last_char)
    
    # 한글 유니코드 범위(가 ~ 힣) 내에 있는지 확인
    if 0xAC00 <= last_char_code <= 0xD7A3:
        # 28로 나눈 나머지가 0이면 받침이 없는 것입니다.
        if (last_char_code - 0xAC00) % 28 == 0:
            return "는"
        else:
            return "은"
            
    # 한글이 아니라 영어나 숫자, 특수문자인 경우 기본값 처리
    return "은/는"


class MyError(Exception):
    def __init__(self, nick):
        self.nick = nick

    def __str__(self):
        # 함수를 호출하여 조사(은/는)를 동적으로 결정합니다.
        josa = get_josa_eun_neun(self.nick)
        return f"{self.nick}{josa} 허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == "바보" or nick == "사슴":
        # global 변수 대신 에러 클래스를 생성할 때 직접 별명을 넘겨주는 것이 훨씬 안전합니다.
        raise MyError(nick)
    
    print(nick)


try:
    say_nick(input("별명을 입력하세요 : "))
except MyError as e:
    print(e)