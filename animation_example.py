# include "Animation"
from Animation import Animation
import pyrr
from AnimateModel import Animate


def grip():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    grip = Animation(
        "./hand-animation/grip/hand_sub2_triang", "./texture_test.png", 60, oopos, 2
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


if __name__ == "__main__":
    Animate(flexion)
    Animate(rest)
