N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
t_shirts = 0
for s in sizes :
    t_shirts += (s + T - 1) // T

# 펜
pen_bundle = N // P
pen_single = N % P

print(t_shirts)
print(pen_bundle, pen_single)
