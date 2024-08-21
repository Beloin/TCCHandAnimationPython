# include "Animation"
from Animation import Animation
import pyrr
from AnimateModel import Animate


def configureAnimation():
    o1pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
    grip = Animation(
        "./hand-animation/grip/hand_sub2_triang", "./texture_test.png", 60, o1pos, 2
    )
    return grip


if __name__ == "__main__":
    Animate(configureAnimation)
