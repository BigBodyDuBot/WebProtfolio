from socket import *
import sys

def run_client(server_host: str, server_port: int, filename: str):
    path = filename if filename.startswith("/") else "/" + filename
    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        clientSocket.connect((server_host, server_port))
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {server_host}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        print("\n[i] Sending request:")
        print(request)
        clientSocket.sendall(request.encode())

        chunks = []
        while True:
            data = clientSocket.recv(4096)
            if not data:
                break
            chunks.append(data)
        raw = b"".join(chunks)

        print("\n---- Server Response ----")
        try:
            print(raw.decode("utf-8"))
        except UnicodeDecodeError:
            print(raw.decode("iso-8859-1", errors="replace"))

def interactive_prompt():
    print("No command-line arguments detected; entering interactive mode.\n")
    server_host = input("Server host (e.g., 127.0.0.1): ").strip() or "127.0.0.1"
    while True:
        port_text = input("Server port (e.g., 6789): ").strip() or "6789"
        try:
            server_port = int(port_text)
            break
        except ValueError:
            print("Please enter a valid integer port.")
    filename = input("Filename on server (e.g., HelloWorld.html): ").strip() or "HelloWorld.html"
    return server_host, server_port, filename

def main():
    if len(sys.argv) == 4:
        server_host = sys.argv[1]
        try:
            server_port = int(sys.argv[2])
        except ValueError:
            print("Port must be an integer.")
            sys.exit(1)
        filename = sys.argv[3]
        run_client(server_host, server_port, filename)
    else:
        server_host, server_port, filename = interactive_prompt()
        run_client(server_host, server_port, filename)

if __name__ == "__main__":
    main()


