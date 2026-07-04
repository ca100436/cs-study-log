# 이메일 주소에서 아이디와 도메인 구분하기
'''
email = input("이메일을 입력하세요 : ")

parts = email.split("@")

print(parts[0])
print(parts[1])
'''
# 쇼핑리스트 입력받아서 오름차순 정렬하기
'''
shopping_list = []

for i in range(4) :
    item = input("Shopping_list(i+1)을 입력하세요 : ")
    shopping_list.append(item)

shopping_list.sort()
print("쇼핑목록", shopping_list)
'''
# 딕셔너리로 영한사전 만들기
'''
dic = {
    "one" : "하나",
    "two" : "비율",
    "three" : "셋"
}

word = input("단어를 입력하세요 : ")

if word in dic :
    print(dic[word])
else :
    print("없음")
'''
# 집합(set)으로 두 파티 모두 참석한 사람 찾기
'''
A = {"Shin", "Jannet", "David", "Park"}
B = {"Park", "Jung", "Clark", "Lee", "David"}

print("2개 모두 파티에 참석한 사람은 다음과 같습니다.")
print(A & B)
'''
# 짝수 / 홀수 판별 프로그램
'''
N = int(input("수를 입력하세요 : "))

print(N, "(을)를 입력하셨습니다.")

if N > 0 :
    if N % 2 == 0 :
        print(N, "은(는) 짝수입니다.")
    else :
        print(N, "은(는) 홀수입니다.")
else :
    print("판별할 수 없는 수를 입력하셨습니다.")
'''
# while문으로 별 출력하기
'''
i = 0

while True :
    i += 1
    if i > 5 :
        break
    print("*" * i)
'''