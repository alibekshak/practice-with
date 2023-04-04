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

window = turtle.Screen()
window.bgcolor('orange')
window.tracer(3) # анимация 

balls = []
count = 7

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
    ball.gravitation = random.randint(1, 30)*0.01







while True:
    window.update()
    for ball in balls:
        ball.speedY = ball.speedY - ball.gravitation
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
        
        if ball.ycor() <= -240:
            ball.sety(-240)
            ball.speedY = -ball.speedY

        if ball.xcor() >= 240 or ball.xcor() <= -240:
            ball.speedX = -ball.speedX

window.mainloop()