from ai_paddle import AIPaddle
from user_paddle import UserPaddle
from turtle import Screen
from ball import Ball
import time

def create_screen():
    screen = Screen()
    screen.setup(800, 600, None, None)
    screen.bgcolor('black')
    screen.title('Pong') 
    screen.listen()
    
    return screen

def pong():
    screen = create_screen()
    ai_paddle = AIPaddle()
    user_paddle = UserPaddle()
    ball = Ball()

    game_is_on = True

    screen.onkey(key='Up',     fun=user_paddle.move_up)
    screen.onkey(key='Down',   fun=user_paddle.move_down)
    screen.onkey(key='Delete', fun=screen.exitonclick)
    
    while game_is_on:
        screen.update()
        ball.move_ball()
        ai_paddle.move()

        # Ball collision with wall

        if ball.ycor() > 300:
            pass
        



if __name__ == "__main__":
    pong()
