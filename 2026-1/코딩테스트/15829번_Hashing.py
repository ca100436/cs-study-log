L = int(input())
words = input()

result = 0

for i in range(L) :
    value = ord(words[i]) - 96     # a를 1로 만들기
    result += value * (31 ** i)

print(result % 1234567891)
