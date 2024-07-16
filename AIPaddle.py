import turtle

UP = 90
DOWN = 270

class AIPaddle:
    def __init__(self):
        self.ai_paddle = self.create_paddle()
        self.direction = UP
        
    def create_paddle(self):

        paddle = turtle.Turtle(
            shape='square',
            visible=True,
        )
    
        paddle.color('White')
        paddle.resizemode('user')
        paddle.shapesize(1, 5)
        paddle.penup()
        paddle.speed('fastest')
        paddle.goto(x=350,y=0)
        paddle.setheading(UP)
        
        return paddle
    
    def move(self):
        cur_pos = self.ai_paddle.pos()

        # Reached the top of the screen, needs to go down now
        if cur_pos[1] == 240:
            self.ai_paddle.setheading(DOWN)
        
        # Reached the bottom
        elif cur_pos[1] == -240:
            self.ai_paddle.setheading(UP)
        
        self.ai_paddle.fd(20)

