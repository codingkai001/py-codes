from bs4 import BeautifulSoup
import requests
from multiprocessing import Process
import time

BASE_URL = 'https://www.qu.la/book/111983/'
PAGE_RANGE = range(5788579, 5788598)

if __name__ == '__main__':
    for page in PAGE_RANGE:
        html = requests.get(BASE_URL + str(page) + '.html')
        print('正在爬取第' + str(page - 5788567) + '章。。。')
        bs = BeautifulSoup(html.text, 'html.parser')
        content = bs.find('div', attrs={'id': 'content'}).get_text()
        title = bs.find('title').get_text()
        with open(title + '.txt', 'wt', encoding='utf-8') as f:
            f.write(content)
        print(title + ' 爬取完成。。。')
        time.sleep(5)
