from Paddle import Paddle
import time

class UserPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__(xpos=-350)
        self.last_input_time = 0
        self.__INPUT_DELAY = 0.1

    def move_up(self) -> None:
        time_now = time.time()

        if time_now - self.last_input_time > self.__INPUT_DELAY:
            self.last_input_time = time_now
            super().move_up()
        
    def move_down(self) -> None:
        time_now = time.time()

        if time_now - self.last_input_time > self.__INPUT_DELAY:
            self.last_input_time = time_now
            super().move_down()
    