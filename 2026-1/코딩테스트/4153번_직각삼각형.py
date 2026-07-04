while True :
    a, b, c = map(int, input().split())

    if a == 0 and b == 0  and c == 0 :
        break

    a, b, c = sorted([a, b, c])

    if a*a + b*b == c*c :
        print("right")
    else :
        print("wrong")
