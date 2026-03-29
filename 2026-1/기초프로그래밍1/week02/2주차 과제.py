import turtle as t

t.shape("turtle")
t.speed(5)
t.pensize(3)

# 1. 세모, 네모, 동그라미 그리기

# 네모
t.penup()
t.goto(-120, 50)
t.pendown()

for i in range(4) :
    t.forward(100)
    t.left(90)

# 세모
t.penup()
t.goto(0, 50)
t.pendown()

for i in range(3) :
    t.forward(100)
    t.left(120)

# 동그라미
t.penup()
t.goto(-20, -80)
t.pendown()
t.circle(40)

# 2. 별모양
t.penup()
t.goto(150, 100)
t.pendown()

for i in range(5) :
    t.forward(100)
    t.left(144)

# 3. 오각형
t.penup()
t.goto(120, -120)
t.pendown()

for i in range(5) :
    t.forward(100)
    t.left(72)

# 4. 오륜기
t.pensize(5)

# 파랑
t.pencolor("blue")
t.penup()
t.goto(-200, -220)
t.pendown()
t.circle(40)

# 검정
t.pencolor("black")
t.penup()
t.goto(-100, -220)
t.pendown()
t.circle(40)

# 빨강
t.pencolor("red")
t.penup()
t.goto(0, -220)
t.pendown()
t.circle(40)

# 노랑
t.pencolor("yellow")
t.penup()
t.goto(-150, -260)
t.pendown()
t.circle(40)

# 초록
t.pencolor("green")
t.penup()
t.goto(-50, -260)
t.pendown()
t.circle(40)

t.hideturtle()
t.done()