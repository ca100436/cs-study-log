A, B, C = map(int, input().split())

# 1. 세 개 다 같은 경우
if A == B == C :
    print(10000 + A * 1000)

# 2. 두 개만 같은 경우
elif A == B or A == C :
    print(1000 + A * 100)
elif B == C :
    print(1000 + B * 100)

# 3. 모두 다른 경우
else :
    print(max(A, B, C) * 100)
