import time
from Paddle import Paddle

UP = 90
DOWN = 270

class AIPaddle(Paddle):
    def __init__(self):
        super().__init__(xpos=350)
        self.last_movement = 0
        self.__INPUT_DELAY = 0.1 # 100ms

    def move(self):
        time_now = time.time()

        # Paddle move delay
        if time_now - self.last_movement > self.__INPUT_DELAY:
            self.last_movement = time_now
            
            # Reached top of the screen?
            if self.paddle.ycor() >= 240:
                self.paddle.seth(DOWN)
            
            # Reached bottom of the screen?
            if self.paddle.ycor() <= -240:
                self.paddle.seth(UP)
            
            # Actual movement - Determines which direction paddle needs to go
            if self.paddle.heading() == DOWN:
                super().move_down()
            elif self.paddle.heading == UP:
                super().move_up()
            # All else fails, go up
            else:
                self.paddle.seth(UP)
                super().move_up()
