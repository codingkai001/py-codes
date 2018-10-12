import socket
import sys

"""
UDP socket服务器端
"""
# UDP数据报最大传送单元为64KB
BUFF_SIZE = 65535
if __name__ == '__main__':
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 5555))
    print("正在监听{}".format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(BUFF_SIZE)
        print("接收到来自客户端{}的数据：{}".format(address, data.decode('utf-8')))
        response = "数据成功发送到服务器，长度为{}".format(len(data))
        sock.sendto(b'#' * 66000, address)
