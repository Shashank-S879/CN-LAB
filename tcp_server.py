import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 65432
BASE_DIR = Path(__file__).resolve().parent

def handle_client(conn, address):
    with conn:
        print(f"Connected by {address}")
        request = bytearray()
        while b"\\n" not in request and len(request) < 1024:
            part = conn.recv(1024)
            if not part:
                break
            request.extend(part)

        filename = request.decode("utf-8", errors="replace").split("\\n", 1)[0].strip()
        path = (BASE_DIR / filename).resolve()

        # Keep requested files inside this program's folder.
        if path.parent != BASE_DIR or not path.is_file():
            conn.sendall(b"ERROR: File not found.")
            return

        with path.open("rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                conn.sendall(data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"TCP server listening on {HOST}:{PORT}")
        print(f"Requestable files must be in: {BASE_DIR}")
        try:
            while True:
                conn, address = server.accept()
                handle_client(conn, address)
        except KeyboardInterrupt:
            print("\\nTCP server stopped.")

if __name__ == "__main__":
    main()
