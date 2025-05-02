# Default Paddle that the AI and User Paddle will be derived from
import turtle

class Paddle:
    def __init__(self, xpos):

        self.paddle = turtle.Turtle(
            shape='square',
            visible=False,
        )
    
        self.paddle.color('White')
        self.paddle.resizemode('user')
        self.paddle.shapesize(1, 5)
        self.paddle.penup()
        self.paddle.speed('fastest')
        self.paddle.goto(x=xpos, y= 0)
        self.paddle.seth(90)
        self.paddle.showturtle()

    def move_up(self):
        y_cor = self.paddle.ycor()

        if y_cor < 240:
            self.paddle.goto(x=self.paddle.xcor(), y= y_cor + 20)
    
    def move_down(self):
        y_cor = self.paddle.ycor()

        if y_cor > -240:
            self.paddle.goto(x=self.paddle.xcor(), y= y_cor - 20)
    