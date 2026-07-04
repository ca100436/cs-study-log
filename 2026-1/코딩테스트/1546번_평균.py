# 풀이 1

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

new_scores = []

for s in scores :
    new_scores.append(s / max_score * 100)

print(sum(new_scores) / N)

# 풀이 2

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

total = 0

for s in scores :
    total += s / max_score * 100

print(total / N)
