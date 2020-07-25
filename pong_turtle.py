import turtle
import random
import winsound


"""initializing"""
window = turtle.Screen()
window.title('pong')
window.bgpic('photos/bg.png')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)


"""paddle_A"""
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.color('red')
paddle_A.penup()
paddle_A.goto(-350, 0)
paddle_A_point = 0

"""paddle_B"""
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape('square')
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.color('blue')
paddle_B.penup()
paddle_B.goto(350, 0)
paddle_B_point = 0

"""ball"""
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('green')
ball.penup()
ball.goto(0, 0)
ball_dx = 0.5
ball_dy = 0.5


"""paddle a up_down"""


def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


"""paddle B up_down"""


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


"""paddle movement"""
window.listen()
"""paddle a"""
window.onkeypress(paddle_A_up, 'w')
window.onkeypress(paddle_A_down, 's')
"""paddle b"""
window.onkeypress(paddle_B_up, 'Up')
window.onkeypress(paddle_B_down, 'Down')

"""pen"""
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'player A:{paddle_A_point}  player B:{paddle_B_point}',
          align='center', font=('Courier', 24, 'normal'))


"""mainloop"""

try:
    while True:
        window.update()
        ball.setx(ball.xcor()+ball_dx)
        ball.sety(ball.ycor()+ball_dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball_dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_dx *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball_dy *= -1

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_dx *= -1

        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_B.ycor()+50 and ball.ycor() > paddle_B.ycor()-50:

            paddle_B_point += 1
            pen.clear()
            pen.write(f'player A:{paddle_A_point}  player B:{paddle_B_point}',
                      align='center', font=('Courier', 24, 'normal'))

            ball.setx(340)
            ball_dx *= -1

        if ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() > paddle_A.ycor()-50 and ball.ycor() < paddle_A.ycor()+50:
            paddle_A_point += 1
            pen.clear()
            pen.write(f'player A:{paddle_A_point}  player B:{paddle_B_point}',
                      align='center', font=('Courier', 24, 'normal'))

            ball.setx(-340)
            ball_dx *= -1
            # winsound.PlaySound('point.wav', winsound.SND_ASYNC)
except:
    print('')

