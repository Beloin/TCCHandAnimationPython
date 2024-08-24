import enum

from glfw import make_context_current
import pyrr

from Animation import Animation, TickModel
from model import Model


def grip():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    grip = Animation(
        "./hand-animation/grip/grip", "./models/Hand/base_texture.png", 60, oopos, 2
    )
    return grip

def flexion():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    flexion = Animation(
        "./hand-animation/flexion/flexion", "./models/Hand/base_texture.png", 60, oopos, 2
    )
    return flexion

def rest():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    rest = Animation(
        "./hand-animation/rest/rest", "./models/Hand/base_texture.png", 1, oopos, 2
    )
    return rest



class AnimationName(enum.Enum):
    FLEXION = 2
    GRIP = 1
    REST = 0


class AnimationControl(TickModel):
    def __init__(self) -> None:
        self._grip = grip()
        self._flexion = flexion()
        self._rest = rest()

        self._current_animation: Animation = self._rest

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
