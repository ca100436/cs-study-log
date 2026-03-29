# 1) replace 함수 이용

s = "a:b:c:d"
result = s.replace(":", "#")
print(result)

# 2) split 함수와 join 함수 이용

s = "a:b:c:d"
s.split(":")
print(s.split(":"))
s.join(":")
print(s.join("a:b:c:d"))

# 3) 고급 문자열 포멧팅 실행 결과

print("Looks like {1} and {0} for breakfast" .format("eggs", "spam"))
print("There is {0} {1} {2} {3}" .format(1, "spam", 4, "you"))
print("Hello {0}" .format("Susan", "Computewell"))
