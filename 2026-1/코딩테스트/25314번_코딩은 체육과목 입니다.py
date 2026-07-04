# 방법 1

N = int(input())

for _ in range(N // 4) :
    print("long", end = " ")

print("int")

# 방법 2

N = int(input())
print("long " * (N // 4) + "int")

