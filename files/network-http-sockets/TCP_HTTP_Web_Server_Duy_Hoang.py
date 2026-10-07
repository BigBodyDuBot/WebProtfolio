# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverPort = 6789
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024).decode()
        # Fill in end

        filename = message.split()[1]
        f = open(filename[1:], 'r', encoding='utf-8')

        # Fill in start
        outputdata = f.read()
        # Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        header = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(outputdata.encode())}\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        connectionSocket.send(header.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        body = (
            "<html><head><title>404 Not Found</title></head>"
            "<body><h1>404 Not Found</h1>"
            "<p>The requested file was not found on this server.</p>"
            "</body></html>"
        )
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            f"Content-Length: {len(body.encode())}\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{body}"
        )
        connectionSocket.send(response.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
