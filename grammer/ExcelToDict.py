with open(R"C:\Users\Coding-Kai\Desktop\excel\某些领域学士学位授予情况.csv", "rt") as f:
    dic = {}
    for line in f:
        data = line.split(',')
        dic[data[0]] = (data[1], data[2])
request = input("请输入要查找的领域：")
print("研究领域".ljust(17, ' '), "1981年".ljust(10, ' '), "2010年".ljust(10, ' '), sep='')
print("-".ljust(37, '-'))
if request in dic:
    print(request.ljust(20, ' '), dic[request][0].ljust(10, ' '), dic[request][1].ljust(10, ' '), sep='')
else:
    print("无相关信息！")
