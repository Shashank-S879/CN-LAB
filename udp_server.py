import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5005
MAX_DATAGRAM = 60000
BASE_DIR = Path(__file__).resolve().parent

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((HOST, PORT))
        print(f"UDP server listening on {HOST}:{PORT}")
        print(f"Requestable files must be in: {BASE_DIR}")
        try:
            while True:
                request, client_address = server.recvfrom(1024)
                filename = request.decode("utf-8", errors="replace").strip()
                print(f"Client requested: {filename}")
                path = (BASE_DIR / filename).resolve()

                if path.parent != BASE_DIR or not path.is_file():
                    response = b"ERROR: File not found."
                else:
                    data = path.read_bytes()
                    response = data if len(data) <= MAX_DATAGRAM else b"ERROR: File too large for this simple UDP example."
                server.sendto(response, client_address)
        except KeyboardInterrupt:
            print("\\nUDP server stopped.")

if __name__ == "__main__":
    main()
