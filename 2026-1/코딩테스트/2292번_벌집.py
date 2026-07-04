N = int(input())

layer = 1    # 현재 겹 수
end = 1     # 현재 겹의 마지막 번호

while N > end :
    end += 6 * layer
    layer += 1

print(layer)
