import enum
from typing import Union

from glfw import make_context_current
import pyrr

from Animation import Animation, TickModel
from model import Model

ANIMATION_THRESHOLD = 99


def grip():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    grip = Animation(
        "./hand-animation/grip/grip", "./models/Hand/base_texture.png", 60, oopos, 2
    )
    return grip


def flexion():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    flexion = Animation(
        "./hand-animation/flexion/flexion",
        "./models/Hand/base_texture.png",
        60,
        oopos,
        2,
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
        self._next_animation = None
        self._animation_needs_change = False

    def tick(self, time=0):
        self._current_animation.tick(time)
        self._internal_animation_change()

    def model(self) -> Model:
        return self._current_animation.model()

    def change_animation(self, animation: AnimationName):
        match animation:
            case AnimationName.FLEXION:
                self._next_animation = self._flexion
            case AnimationName.GRIP:
                self._next_animation = self._grip
            case AnimationName.REST:
                self._next_animation = self._rest

        self._animation_needs_change = True

    def _internal_animation_change(self):
        if self._animation_needs_change:
            if self._current_animation.animation_percentage() >= ANIMATION_THRESHOLD:
                self._current_animation.reset()
                self._current_animation = self._next_animation
                self._animation_needs_change = False
