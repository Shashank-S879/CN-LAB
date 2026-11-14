import socket

HOST = "127.0.0.1"
PORT = 65432

def main():
    filename = input("Enter file name to request: ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return

    try:
        received = bytearray()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.sendall((filename + "\\n").encode("utf-8"))
            while True:
                data = client.recv(4096)
                if not data:
                    break
                received.extend(data)

        print("\\n--- File Content / Server Response ---")
        print(received.decode("utf-8", errors="replace"))
    except ConnectionRefusedError:
        print("Could not connect. Start tcp_server.py first.")
    except OSError as error:
        print(f"Network error: {error}")

if __name__ == "__main__":
    main()
