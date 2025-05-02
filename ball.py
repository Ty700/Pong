import turtle

class Ball:
    def __init__(self) -> None:
        self.ball = turtle.Turtle(shape='circle')
        self.ball.goto(0,0)
        self.ball.speed('fast')
        self.ball.penup()
        self.ball.color('white')
        self.ball.FloatY = 0
        self.ball.FloatX = 0

    def move_ball(self):
        # A few things we first want to move the ball towards the player, so left
        # If the player hits it on the top half of the paddle, the ball will move in a leftward trajectory
        # If the player hits it on the bottom half, the ball will move in a rightward trajectory
        # If the player hits it somewhere near the middle, the ball will go horizontal

        new_x = self.ball.xcor() + 10
        new_y = self.ball.ycor() + 10
        self.ball.goto(new_x, new_y)
        
