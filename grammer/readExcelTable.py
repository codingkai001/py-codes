# info = str(input("请输入要查找的关键字："))
count = 0
with open(R"C:\Users\Coding-Kai\Desktop\excel\班服.csv", "rt") as f:
    for line in f:  # 按行读取csv文件
        # data = line.split(',')  # 将每一行用逗号分隔成一个列表
        if 'M' in line:
            # count += 1
            print(line)

"""
XS-1
S-3
M-7
L-13
XL-8
XXL-4
"""
