import socket
import sys

"""TCP socket客户端Demo"""
SOCK_BUFFER = 1024 * 10

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))
    sys.stdout.write(client.recv(SOCK_BUFFER).decode() + "\n")
    while True:
        request = input(">>>").strip()
        if request == "":
            pass
        elif request == "exit":
            client.send(request.encode("utf-8"))
            client.close()
            sys.exit(0)
        else:
            client.sendall(request.encode("utf-8"))
            response = client.recv(SOCK_BUFFER)
            sys.stdout.write(response.decode() + "\n")
