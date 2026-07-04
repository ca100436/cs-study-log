# 방법 1 (문자열로 처리)
A = int(input())
B = input()    # 문자열로 받기

print(A * int(B[2]))    # 일의 자리
print(A * int(B[1]))    # 십의 자리
print(A * int(B[0]))    # 백의 자리 
print(A * int(B))       # 전체 곱


# 방법 2 (숫자로 처리)
A = int(input())
B = int(input())

print(A * (B % 10))                 # 일의 자리
print(A * ((B // 10) % 10))        # 십의 자리
print(A * (B // 100))               # 백의 자리
print(A * B)
