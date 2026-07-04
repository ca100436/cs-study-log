isbn = input().strip()

total = 0
star_idx = -1

for i in range(13):
    if isbn[i] == '*':
        star_idx = i
        continue

    num = int(isbn[i])

    if i % 2 == 0:
        total += num
    else:
        total += num * 3

for x in range(10):
    if star_idx % 2 == 0:
        check = total + x
    else:
        check = total + x * 3

    if check % 10 == 0:
        print(x)
        break
