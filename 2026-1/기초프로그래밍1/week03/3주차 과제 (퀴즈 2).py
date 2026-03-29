jumin = "881120-1068234"

# 1) 연월일 부분과 그 뒤의 숫자 부분 나누기

birth = jumin[:6]
back = jumin[7:]

print("연월일 출력 : ", birth)
print("뒤의 숫자 부분 : ", back)

# 2) 성별을 나타내는 숫자 출력

gender = jumin[7]
print("성별을 나타내는 숫자 : ", gender)
