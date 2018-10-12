import socket

"""手写header模拟http请求，下载响应内容"""
request_header = """\
GET /s?wd=福州大学 HTTP/1.1\r\n\
Host: www.baidu.com\r\n\
User-Agent: pythonSocket\r\n\
Connection: close\r\n\r\n\
"""
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("www.baidu.com", 80))
conn.send(request_header.encode('utf-8'))

buffer = []
while True:
    data = conn.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
response = b''.join(buffer)
header, body = response.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# with open("baidu.html", "wb") as f:
#     f.write(body)
