import socket
import os
import sys

"""基本的socket服务器端（阻塞性，同一时间只能处理单个请求）TCP连接Demo"""
SOCK_BUFFER = 1024 * 10
# 创建套接字对象，AF_INET为socket协议，SOCK_STREAM为TCP，SOCK_DGRAM为UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 将监听的地址（主机名、端口号对）绑定到套接字上，端口号范围：0~65535
server.bind(('127.0.0.1', 8000))
'''设置并启动TCP监听器,在等待队列中允许放置的进来的连接总数为10，
等待队列最大值socket.SOMAXCONN=2147483647。当等待队列已满时，客户端将被告知拒绝连接
'''
server.listen(1)
sys.stdout.write("服务器初始化完成...\n")

while True:
    """等待连接的到来（阻塞式），被动接受客户端的TCP连接
    返回元组（连接对象，客户端地址）
    """
    conn, addr = server.accept()
    ip, port = addr
    sys.stdout.write("接收到来自%s:%s的客户端连接...\n" % (ip, port))
    conn.send("成功连接至服务器...".encode('utf-8'))
    while True:
        sys.stdout.write("正在等待客户端的请求...\n")
        data = conn.recv(SOCK_BUFFER)
        if data.decode() == "exit":
            # server.shutdown(0)   # 关闭连接,参数0阻止socket接收数据，1阻止发送，2阻止接收和发送
            sys.stdout.write("客户端连接已断开...\n")
            conn.close()
            break
        sys.stdout.write("来自客户端的请求：%s\n" % data.decode())
        # cmd_res = os.popen(data.decode()).read()  # 接收字符串，执行指令
        # print("successfully send %d Byte" % len(cmd_res))
        conn.sendall("请求已成功处理...".encode('utf-8'))
        # if len(cmd_res) == 0:
        #     cmd_res = "cmd has no output..."
        # conn.send(cmd_res.encode("utf-8"))
