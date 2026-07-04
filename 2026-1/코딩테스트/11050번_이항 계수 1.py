# 풀이 방법 1 (팩토리얼 사용)
'''
import math

N, K = map(int, input().split())

print(math.factorial(N) // (math.factorial(K) * math.factorial(N-K)))
'''
# 풀이 방법 2 (직접 구현 버전)
'''
def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

N, K = map(int, input().split())

print(factorial(N) // (factorial(K) * factorial(N-K)))
'''
