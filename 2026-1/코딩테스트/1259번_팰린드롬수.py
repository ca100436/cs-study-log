# 문자열 뒤집기

while True :
    num = input()

    if num == '0' :
        break

    if num == num[: : -1] :
        print("yes")
    else :
        print("no")

# 직접 비교하기

while True :
    num = input()

    if num == '0' :
        break

    is_palindrome = True

    for i in range(len(num) // 2) :
        if num[i] != num[-(i + 1)] :
            is_palindrome = False
            break

        if is_palindrome :
            print("yes")
        else :
            print("no")
