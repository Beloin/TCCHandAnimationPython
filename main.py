import threading
from AnimationControl import AnimationControl
import server.AnimationControlServer as server
from AnimateModel import Animate

controller = None
thd = threading.Thread(target=server.listen, args=(controller,))

def configure_controller():
    global controller
    controller = AnimationControl()
    return controller

def main():
    thd.start()
    Animate(configure_controller)

if __name__ == "__main__":
    main()
