import socket

"""UDP客户端"""
BUFF_SIZE = 65535
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("请输入要发送的数据：")
        sock.sendto(message.encode('utf-8'), ('127.0.0.1', 5555))
        data, address = sock.recvfrom(BUFF_SIZE)
        print(data.decode('utf-8'))
