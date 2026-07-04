# Quiz-1. 파일을 읽어서 줄 번호 붙여서 저장

infile = open("lovepoems.txt", "r")
outfile = open("output.txt", "w")

lines = infile.readlines()

for i, line in enumerate(lines, start = 1):
    outfile.write(str(i) + ":" + line)

infile.close()
outfile.close()

# Quiz-2. 문자 개수 세기

infile = open("lovepoems.txt", "r")

text = infile.read()
char_count = {}

for ch in text :
    if ch in char_count :
        char_count[ch] += 1
    else :
        char_count[ch] = 1

print(char_count)
infile.close()

# Quiz-3. CSV 파일 읽기

infile = open("data.csv", "r")

for line in infile :
    data = line.strip().split(",")

    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])

infile.close()