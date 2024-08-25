# TODO: How wil the communcation work?
import socket

HOST = "127.0.0.1"
PORT = 9191

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Input type is MOVEMENT:GRIP\0 --> Null terminated string
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
