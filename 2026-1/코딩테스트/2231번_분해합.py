N = int(input())    # 우리가 만들고 싶은 최종값

# 1부터 N까지 하나씩 후보를 확인
for i in range(1, N+1) :
    
    total = i    # 분해합 = 자기 자신부터 시작

    # i를 문자열로 바꿔서 각 자리수를 하나씩 꺼냄
    for digit in str(i) :
        total += int(digit)    # 자리수를 숫자로 바꿔서 더함

    # 분해합이 N이랑 같으면 정답!
    if total == N :
        print(i)    # 생성자 출력
        break

# 끝까지 못 찾으면 0 출력
else :
    print(0)
