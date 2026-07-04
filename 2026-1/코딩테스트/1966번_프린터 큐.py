from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((i, priorities[i]) for i in range(n))
    count = 0

    while q :
        idx, priority = q.popleft()

        # 현재 큐 안에 더 높은 중요도가 있으면 뒤로 보냄
        if any(priority < x[1] for x in q) :
               q.append((idx, priority))
        else :
            count += 1
            if idx == m :
                print(count)
                break
