from AnimationControl import AnimationControl, AnimationName
import socket

HOST = "localhost"
PORT = 7777


def listen(animation_control: AnimationControl):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # TODO: Use null terminated string or fixed lenghr
                # Input type is GRIP\0 --> Null terminated string
                data = conn.recv(25)
                if not data:
                    print("Connection closed")
                    break
                mov = data.decode()
                control(mov, animation_control)

    print("Server closed")


def control(mov: str, animation_control: AnimationControl):
    mov = str(mov.strip())
    print('Got: "', mov, '" type=', type(mov), sep="")
    if "FLEXION" == mov:
        print("FLEXION")
        animation_control.change_animation(AnimationName.FLEXION)
    elif "GRIP" == mov:
        print("GRIP")
        animation_control.change_animation(AnimationName.GRIP)
    elif "REST" == mov:
        print("REST")
        animation_control.change_animation(AnimationName.REST)
