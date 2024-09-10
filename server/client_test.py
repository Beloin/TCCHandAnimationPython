import socket


def sanitize(v: str):
    for _ in range(25 - len(v)):
        v += "\0"

    return v


def connect(addr: str, port: int) -> socket.socket:
    conn = socket.create_connection((addr, port))
    return conn


def send_movement(conn: socket.socket, mov: str):
    bts = sanitize(mov).encode()
    conn.sendall(bts)


def main():
    with connect("localhost", 7777) as conn:
        while True:
            mov = input("Write movement: (FLEXION, GRIP, REST): ")
            while mov not in ["FLEXION", "GRIP", "REST"]:
                mov = input("Please, write again: ")

            send_movement(conn, mov)


if __name__ == "__main__":
    main()
