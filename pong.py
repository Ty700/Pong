from AIPaddle import AIPaddle
from UserPaddle import UserPaddle
from turtle import Screen
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

    game_is_on = True

    screen.onkey(key='Up',     fun=user_paddle.move_up)
    screen.onkey(key='Down',   fun=user_paddle.move_down)
    screen.onkey(key='Delete', fun=screen.exitonclick)
    
    while game_is_on:
        screen.update()
        ai_paddle.move()

        
        



if __name__ == "__main__":
    pong()
