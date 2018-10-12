import requests
from bs4 import BeautifulSoup

List = ['军事武器', '农业生产', '科学研究']
# 源码获取
url = 'http://www.nipic.com/photo/index.html'
html = requests.get(url)
# f = open('nipicHtml.txt', 'w', encoding='utf-8')
# f.write(html.text)
bs = BeautifulSoup(html.text, "html.parser")
alist = bs.find_all('a')  # 获取所有的a标签
cnt = 1
for a in alist:
    for i in List:
        if a.string == i:
            url = 'http://www.nipic.com' + a['href']
            html = requests.get(url)  # 获取子url
            bs = BeautifulSoup(html.text, "html.parser")
            _alist = bs.find_all('a')
            for _a in _alist:
                if _a.img is not None:
                    pic = requests.get(_a.img['src'])  # 下载图片
                    f = open(r'C:\Users\Coding-Kai\Desktop\爬虫图片\昵图网' + '\\' + a.string + '\\' + str(cnt) + '.jpg', 'wb')
                    f.write(pic.content)
                    f.close()
                    cnt += 1
