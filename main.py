import threading
from AnimationControl import AnimationControl
import server.AnimationControlServer as server
from AnimateModel import Animate


def configure_controller():
    controller = AnimationControl()
    thd = threading.Thread(target=server.listen, args=(controller,))
    thd.start()
    return controller


def main():
    Animate(configure_controller)


if __name__ == "__main__":
    main()
