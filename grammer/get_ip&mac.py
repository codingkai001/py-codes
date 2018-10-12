import uuid
import socket


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


print(get_mac_address())

# 得到用户名
my_name = socket.getfqdn(socket.gethostname())
print(my_name)
# 得到地址
my_add = socket.gethostbyname(my_name)
print(my_add)
