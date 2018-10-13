import array

with open(r'E:\代码\web\img\favicon.png', 'rb') as f:
    data = f.read()
print(len(data))  # 34360个字节大小的图片
