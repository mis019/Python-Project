def check_age(age):
    if age < 0:
        # 나이가 음수일 때 의도적으로 ValueError를 발생시킵니다.
        raise ValueError("나이는 음수가 될 수 없습니다!")
    print(f"당신의 나이는 {age}살입니다.")

try:
    check_age(50)
except ValueError as e:
    print(f"오류 발생: {e}")
