# 풀이 1
'''
A, B, V = map(int, input().split())

day = (V - A) // (A - B)

if (V - A) % (A - B) != 0 :
    day += 1

print(day + 1)
'''
# 풀이 2
'''
A, B, V = map(int, input().split())

print((V - A) + (A - B - 1)) // (A - B) + 1)
'''
