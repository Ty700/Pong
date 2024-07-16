import turtle

UP = 90
DOWN = 270

class AIPaddle:
    def __init__(self):
        self.ai_paddle = self.create_paddle()
        self.direction = UP

    def create_paddle(self):

        new_paddle = turtle.Turtle(
            shape='square',
            visible=False,
        )

        new_paddle.color('White')
        new_paddle.resizemode('user')
        new_paddle.shapesize(1, 5)
        new_paddle.penup()
        new_paddle.speed('fastest')
        new_paddle.goto(x=350,y=0)
        new_paddle.setheading(UP)
        
        # Paddle is created in invisible mode so we don't see the setup
        # Now that all the paddle configs are made, we can show it
        new_paddle.showturtle()

        return new_paddle

    def move(self):
        cur_pos = self.ai_paddle.pos()

        # Reached the top of the screen, needs to go down now
        if cur_pos[1] == 240:
            self.ai_paddle.setheading(DOWN)
        
        # Reached the bottom
        elif cur_pos[1] == -240:
            self.ai_paddle.setheading(UP)
        
        self.ai_paddle.fd(20)

