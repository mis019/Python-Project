import sys
import os

# 1. \P 경고 해결 (r 추가) 및 모듈 검색 경로 추가
sys.path.append(r"E:\Python Project\chapter5")

students = ["김철수", "이영희", "박민수", "최유진"]

# 파일들이 모여있는 폴더 경로를 변수로 지정합니다. (r을 붙이거나 /를 사용)
TARGET_DIR = r"E:\Python Project\chapter5"

for student in students:
    try:
        # os.path.join을 사용하면 폴더 경로와 파일 이름을 안전하게 합쳐줍니다.
        # 결과값 예시: "E:\Python Project\chapter5\김철수_성적.txt"
        file_path = os.path.join(TARGET_DIR, f"{student}_성적.txt")
        
        with open(file_path, "r", encoding="utf-8") as file:
            score = file.read()
            print(f"{student}의 성적 : {score}")

    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 다음으로 건너뜁니다.")
        # 반복문의 맨 마지막 줄이므로 continue는 생략해도 무방합니다.