T = int(input())    # 테스트 케이스 개수

for _ in range(T):
    k = int(input())    # 층
    n = int(input())    # 호

    # people = [1, 2, 3, . . . , n] 처럼 0층 만들기
    people = [i for i in range(1, n + 1)]

    # 1층부터 k층까지 올라가기
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i - 1]

    # 최종 k층 n호만 출력
    print(people[n - 1])
