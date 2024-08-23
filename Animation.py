from model import Model, create_model
import math


class Animation:
    def __init__(
        self,
        fileprefix: str,
        texture: str,
        frames: int,
        pos,
        animation_time=2,
        reverse=False,
    ):
        self._models = []
        for i in range(frames):
            filename = fileprefix + str(i + 1).zfill(4) + ".obj"
            self._models.append(create_model(filename, texture, pos))

        self._current_index = 0
        self._frames = frames
        self._animation_time = animation_time
        self._reverse = reverse
        self._order = 1
        self._last_index = 0

    def tick(self, time=0):
        """
        @param time - In milisseconds
        """
        self._last_index = self._current_index

        if self._current_index >= self._frames:
            self._current_index = 0

        # TODO: get in ms and get the rest of the division to see which part of the animation should be at rn
        if time > 0:
            curr = time % (self._animation_time * 1000)
            # an_time -> frames
            # curr    -> X
            x = (curr * self._frames) / (self._animation_time * 1000)

            # Changes animation order
            if self._last_index > x:
                self._order = 1 if self._order == -1 else -1
                print("Reverting order: ", self._order)

            self._last_index = self._current_index
            self._current_index = math.floor(x)
            return

        new_index = self._current_index + 1
        if self._last_index > new_index:
            self._order = 1 if self._order == -1 else -1
            print("Reverting order: ", self._order)

        self._current_index = new_index

    def get_current_model(self):
        print("Current Frame: ", self._current_index + 1)
        index = self._current_index * self._order
        if self._order == -1 and index == 0:
            index = self._frames - 1
        return self._models[index]

    def reset(self):
        self._current_index = 0
        self._last_index = 0
        self._order = 1

