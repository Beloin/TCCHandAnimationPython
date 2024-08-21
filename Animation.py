from model import Model, create_model
import math


class Animation:
    def __init__(
        self, fileprefix: str, texture: str, frames: int, pos, animation_time=2
    ):
        self._models = []
        for i in range(frames):
            filename = fileprefix + str(i+1).zfill(4) + ".obj"
            self._models.append(create_model(filename, texture, pos))

        self._current_index = 0
        self._frames = frames
        self._animation_time = animation_time

    def tick(self, time=0):
        """
        @param time - In milisseconds
        """
        if self._current_index >= self._frames:
            self._current_index = 0

        # TODO: get in ms and get the rest of the division to see which part of the animation should be at rn
        if time > 0:
            print("Got time: ", time)
            curr = time % (self._animation_time * 1000)
            # an_time -> frames
            # curr -> X
            x = (curr * self._frames) / (self._animation_time * 1000)
            self._current_index = math.floor(x)
            return

        self._current_index += 1

    def get_current_model(self):
        print("Current Frame: ", self._current_index)
        return self._models[self._current_index]
