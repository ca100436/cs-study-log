# 방법 1 (if문)

S = input()

total = 0

for ch in S:
    if ch in "ABC":
        total += 3
    elif ch in "DEF":
        total += 4
    elif ch in "GHI":
        total += 5
    elif ch in "JKL":
        total += 6
    elif ch in "MNO":
        total += 7
    elif ch in "PQRS":
        total += 8
    elif ch in "TUV":
        total += 9
    elif ch in "WXYZ":
        total += 10

print(total)

# 방법 2 (딕셔너리)

dial = {
    "ABC": 3, "DEF": 4, "GHI": 5,
    "JKL": 6, "MNO": 7, "PQRS": 8,
    "TUV": 9, "WXYZ": 10
}

S = input()
total = 0

for ch in S:
    for key in dial:
        if ch in key:
            total += dial[key]

print(total)
