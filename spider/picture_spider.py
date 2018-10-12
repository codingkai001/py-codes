import requests
from bs4 import BeautifulSoup

url = "http://www.wmpic.me/tupian/qingxin"
html = requests.get(url)
# f = open('wmpicMM.txt', 'w', encoding='utf-8')
# f.write(html.text)

bs = BeautifulSoup(html.text, "html.parser")
a_list = bs.find_all('img')  # 匹配img标签
i = 0
for a in a_list:
    f = open(r'C:\Users\Coding-Kai\Desktop\爬虫图片\小清新\wmpic' + str(i + 1) + '.jpg', 'wb')
    if '.jpg' in a['src']:
        pic = requests.get(a['src'])
        f.write(pic.content)  # 二进制写图片
        i += 1
        f.close()
