import socket

HOST = "127.0.0.1"
PORT = 5005
MAX_DATAGRAM = 60000

def main():
    filename = input("Enter filename to request: ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(5)
            client.sendto(filename.encode("utf-8"), (HOST, PORT))
            data, address = client.recvfrom(MAX_DATAGRAM)
        print(f"\\nResponse received from {address}")
        print("--- File Content / Server Response ---")
        print(data.decode("utf-8", errors="replace"))
    except socket.timeout:
        print("No response. Start udp_server.py first.")
    except OSError as error:
        print(f"Network error: {error}")

if __name__ == "__main__":
    main()
