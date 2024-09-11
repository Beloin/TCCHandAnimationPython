from AnimationControl import AnimationControl, AnimationName
import socket

HOST = "localhost"
PORT = 7777


def listen(animation_control: AnimationControl):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(25)
                    if not data:
                        print("Connection closed")
                        break
                    mov = data.decode()
                    mov = mov.replace("\0", "")
                    control(mov, animation_control)

        print("Server closed")


def control(mov: str, animation_control: AnimationControl):
    mov = str(mov.strip()).upper()
    print("Got:", mov)
    if "FLEXION" == mov:
        print("FLEXION")
        animation_control.change_animation(AnimationName.FLEXION)
    elif "GRIP" == mov:
        print("GRIP")
        animation_control.change_animation(AnimationName.GRIP)
    elif "REST" == mov:
        print("REST")
        animation_control.change_animation(AnimationName.REST)
