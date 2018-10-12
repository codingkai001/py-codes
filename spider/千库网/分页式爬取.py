import requests
import time
import os
from bs4 import BeautifulSoup

key = 'MM'  # 搜索的关键字
page_end = 55  # 待爬取的页数

'''待爬取url的列表'''
urls = []
for i in range(1, page_end + 1):
    urls.append('http://588ku.com/sucai/0-default-0-0-xingganmeinv-' + str(i) + '/')

'''按页码循环爬取'''
for url in urls:
    html = requests.get(url)
    bs = BeautifulSoup(html.text, "html.parser")
    alist = bs.find_all('a')
    for a in alist:
        elem = str(a).split(' ')
        if len(elem) >= 7 and 'data-original' in elem[6]:  # 筛选出要爬取素材的url
            # print(elem[6])
            e = elem[6].split('"')
            # print(e[1])
            name = elem[8].split('"')[1]  # 获取图片名称
            # print(name)
            picture = requests.get(e[1])

            f = open(r'C:\Users\Coding-Kai\Desktop\爬虫图片\千库网' + '\\' + key + '\\' + name + '.jpg', 'wb')
            f.write(picture.content)
            f.close()
    print('第' + str(urls.index(url) + 1) + '页' + '爬取完成!')
    time.sleep(2)  # 每爬取一页中止2s
