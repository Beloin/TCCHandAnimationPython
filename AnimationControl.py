import enum

from glfw import make_context_current

from Animation import Animation, TickModel
from animation_example import flexion, grip, rest
from model import Model


class AnimationName(enum.Enum):
    FLEXION = 2
    GRIP = 1
    REST = 0


class AnimationControl(TickModel):
    def __init__(self) -> None:
        self._grip = grip()
        self._flexion = flexion()
        self._rest = rest()

        self._current_animation: Animation = self._grip

    def tick(self, time=0):
        self._current_animation.tick(time)

    def model(self) -> Model:
        return self._current_animation.model()

    def change_animation(self, animation: AnimationName):
        self._current_animation.reset()
        match animation:
            case AnimationName.FLEXION:
                self._current_animation = self._flexion
            case AnimationName.GRIP:
                self._current_animation = self._grip
            case AnimationName.REST:
                self._current_animation = self._rest
