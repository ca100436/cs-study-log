A, B = map(int, input().split())

a, b = A, B

# 최대공약수(GCD) 구하기
while b != 0 :
    a, b = b, a % b

gcd = a

# 최소공배수(LCM) 구하기
lcm = A * B // gcd

print(gcd)
print(lcm)
