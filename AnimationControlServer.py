from AnimationControl import AnimationControl
import socket

HOST = "127.0.0.1"
PORT = 9191


def listen(animation_control: AnimationControl):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # TODO: Use null terminated string or fixed lenghr
                # Input type is MOVEMENT:GRIP\0 --> Null terminated string
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


def control(mov: str, animation_control: AnimationControl):
    match mov:
        case "FLEXION":
            pass
        case "GRIP":
            pass
        case "REST":
            pass
