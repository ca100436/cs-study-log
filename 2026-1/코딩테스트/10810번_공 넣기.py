N, M = map(int, input().split())

basket = [0] * N  # 바구니 초기화

for _ in range(M):
    i, j, k = map(int, input().split())
    
    for x in range(i-1, j):  # 인덱스 맞추기
        basket[x] = k

print(*basket)
