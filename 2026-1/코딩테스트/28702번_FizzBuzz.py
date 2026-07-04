a = input()
b = input()
c = input()

if a.isdigit() :
    num = int(a)
    idx = 1
elif b.isdigit() :
    num = int(b)
    idx = 2
else :
    num = int(c)
    idx = 3

next_num = num + (4 - idx)

if next_num % 15 == 0 :
    print("FizzBuzz")
elif next_num % 3 == 0 :
    print("Fizz")
elif next_num % 5 == 0 :
    print("Buzz")
else :
    print(next_num)
