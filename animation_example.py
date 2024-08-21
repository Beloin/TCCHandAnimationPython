# include "Animation"
from Animation import Animation
import pyrr
from AnimateModel import Animate


def configureAnimation():
    oopos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
    grip = Animation(
        "./hand-animation/grip/hand_sub2_triang", "./texture_test.png", 60, oopos, 2
    )
    return grip


if __name__ == "__main__":
    Animate(configureAnimation)
