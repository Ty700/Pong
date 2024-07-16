from turtle import Screen
from AIPaddle import AIPaddle
import time

def create_screen():
    screen = Screen()

    screen.setup(800, 600, None, None)
    screen.bgcolor('black')
    screen.title('Pong')  
    
    return screen

def pong():
    screen = create_screen() 
    ai_paddle = AIPaddle() 
    # user_padle = UserPaddle()
    
    i = 0
    while i < 100:
        screen.update()
        time.sleep(0.1)
        ai_paddle.move()
        i += 1

    screen.exitonclick()


if __name__ == "__main__":
    pong()
