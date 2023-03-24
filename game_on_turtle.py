import turtle, random

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)

balls = []
count = 5

for i in range(count):

    ball = turtle.Turtle(shape='circle')
    green = random.random()
    blue  = random.random()
    yellow  = random.random()
    ball.color(green, blue, yellow)
    ball.up()
    ball.goto(random.randint(-200, 200), random.randint(100, 280))

    ball.speedY = 0
    ball.speedX = random.randint(-2, 3)
    balls.append(ball)
    window = turtle.Screen()
    window.bgcolor('orange')


gravitation = 0.2


while True:
    for ball in balls:
        ball.speedY = ball.speedY - gravitation
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
        
        if ball.ycor() <= -240:
            ball.speedY = -ball.speedY

        if ball.xcor() >= 240 or ball.xcor() <= -240:
            ball.speedX = -ball.speedX

window.mainloop()