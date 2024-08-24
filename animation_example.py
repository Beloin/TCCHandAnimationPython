# include "Animation"
from time import sleep
from typing import Union

from pygame import threads
from Animation import Animation
import pyrr
from AnimateModel import Animate
from AnimationControl import AnimationControl, AnimationName


def grip():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    grip = Animation(
        "./hand-animation/grip/hand_sub2_triang", "./texture_test.png", 60, oopos, 2
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


def animation_control():
    control = AnimationControl()
    t = threads.Thread(target=animation_thread, args=[control])
    t.start()

    return control

def animation_thread(control: AnimationControl):
    test = 0
    while True:
        sleep(10)
        test += 1

        if test >= 3:
            test = 0

        print("Changing animation")
        control.change_animation(AnimationName(test))


if __name__ == "__main__":
    # Animate(flexion)
    # Animate(rest)

    Animate(animation_control)
