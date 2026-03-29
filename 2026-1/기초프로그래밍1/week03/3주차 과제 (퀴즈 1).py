# 1) 학교이름, 학과, 이름, 연락처 저장 후 출력

univ = "상지대학교"
dept = "컴퓨터공학과"
name = "유성윤"
phone = "010-7369-8876"

print("학교이름 : ", univ)
print("학과 : ", dept)
print("이름 : ", name)
print("연락처 : ", phone)

# 2) 정수 2를 3번 곱한 결과 출력

print("2**3 = ", 2**3)

# 3) 수식 5-(3-1)의 계산 결과 출력

print("5-(3-1) = ", 5-(3-1))

# 4) 두 command 실행 결과 비교

print(2 + 3)
print("2" + "3")

# 5) 국어 80점, 수학 75점, 영어 55점의 평균 출력

kor = 80
math = 75
english = 55
avg = (kor + math + english) / 3
print("평균 = ", avg)

# 6) 자연수가 홀수인지 짝수인지 판별하는 방법

num = int(input("자연수를 입력하세요 : "))

if (num % 2 == 0) :
    print("짝수입니다.")
else :
    print("홀수입니다.")