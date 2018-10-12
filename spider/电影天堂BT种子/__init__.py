from multiprocessing import *
import os
import time
import requests
from bs4 import BeautifulSoup
import re
import sys

index = 0  # 电影资源的序号
save_path = r'F:\python code\LearnPython\Spider\电影天堂BT种子\movie.txt'
f = open(save_path, 'wt', encoding='utf-8')


def excel_init():
    book = Workbook(encoding='gb2312')
    sheet1 = book.add_sheet('movie')
    head = ['片　　名', '译　　名', '年　　代', '产　　地', '类　　别', 'IMDb评分', '片　　长', '简　　介 ', '下载地址']
    row = sheet1.row(0)
    for index, key in enumerate(head):
        row.write(index, key)
    book.save('test.xls')


class MovieSpider:

    def __init__(self, label):
        self.label = label  # 电影类别
        self.pre_url = 'http://www.dytt8.net/html/gndy/'

    def index_req(self):
        base_url = self.pre_url + self.label + '/index.html'
        try:
            url_1 = requests.get(self.pre_url + self.label + '/index.html', timeout=2)  # 添加超时异常处理
            url_1.encoding = 'gb2312'
            soup1 = BeautifulSoup(url_1.text, 'html.parser')

            for tag in soup1.find_all('option'):
                if 'value' in tag.attrs and tag['value'] is not None:
                    url_2 = self.pre_url + self.label + '/' + tag['value']  # 页码url
                    self.page_req(url_2)  # 分页爬取
        except (requests.ConnectTimeout, requests.ReadTimeout):
            print('电影链接{}爬取超时，已自动跳过。。。'.format(base_url))
        except requests.ConnectionError:
            print('服务器连接异常， 已退出程序。。。')
            sys.exit(1)

    def page_req(self, url):
        try:
            url_2 = requests.get(url)  # 超时异常
            url_2.encoding = 'gb2312'
            soup_2 = BeautifulSoup(url_2.text, 'html.parser')

            for a in soup_2.find_all('a'):
                if re.match('^/html/gndy/[a-z]+/.+', a['href']):
                    if 'class' in a.attrs and a['class'][0] == 'ulink':
                        if re.match('.+[0-9]{8}/[0-9]+.html', a['href']):
                            global index
                            index += 1
                            print('正在爬取第{}部电影'.format(index))
                            url_3 = 'http://www.dytt8.net' + a['href']
                            self.detail_req(url_3)  # 爬取内容
        except (requests.ConnectTimeout, requests.ReadTimeout):
            print('电影链接{}爬取超时，已自动跳过。。。'.format(url))
        except requests.ConnectionError:
            print('服务器连接异常， 已退出程序。。。')
            sys.exit(1)

    def detail_req(self, url):
        try:
            url_4 = requests.get(url)
            url_4.encoding = 'gb2312'
            soup = BeautifulSoup(url_4.text, 'html.parser')
            for table in soup.find_all('div'):
                if 'id' in table.attrs and table['id'] == 'Zoom':
                    soup2 = BeautifulSoup(str(table), 'html.parser')
                    p = soup2.find('p')
                    if p is not None:
                        s = str(p).replace('\u3000', ' ').replace('<br/>', '').split('◎')
                        for i in s:
                            if '片  名' in i:
                                f.write(i[5:] + ' ')
                            elif 'IMDb评分' in i:
                                f.write(i[6:] + ' ')
                            elif '简  介' in i:
                                intro = i.split('<')[0]
                                f.write(intro + '\n')

        except (requests.ConnectTimeout, requests.ReadTimeout):
            print('电影链接{}爬取超时，已自动跳过。。。'.format(url))
        except requests.ConnectionError:
            print('服务器连接异常， 已退出程序。。。')
            sys.exit(1)

    '''    def save(self, **kwargs):

        native_name = kwargs['native_name']    # 片名
        foreign_name = kwargs['foreign_name']   # 译名
        peroid = kwargs['peroid']   # 年代
        country = kwargs['country']     # 产地
        category = kwargs['category']   # 类别
        grade = kwargs['grade']     # 评分
        length = kwargs['length']   # 片长
        introduction = kwargs['intro']  # 简介
        # link = kwargs['link']   # 下载地址'''


if __name__ == '__main__':
    # excel_init()
    label = {'日韩电影': 'rihan', '欧美电影': 'oumei',
             '电影制作': 'dyzz', '国内电影': 'china',
             '经典电影': 'jddy'
             }  # 电影类别
    start = time.time()
    p = Pool(cpu_count())  # 进程池对象， arg=同时运行的进程数，为cpu核心数
    for key, value in label.items():
        print('正在爬取{}......'.format(key))
        p.apply_async(MovieSpider(value).index_req())
    p.close()  # 多进程调用结束，不再添加进程
    p.join()  # 等待所有子进程运行完毕
    end = time.time()
    print('爬取完成，用时 %.2f 秒' % (end - start))
    f.close()

'''                            
if '片  名' in i:
    native_name = i[5:]
elif '译  名' in i:
    foreign_name = i[5:]
elif '年  代' in i:
    peroid = i[5:]
elif '产  地' in i:
    country = i[5:]
elif '类  别' in i:
    category = i[5:]
elif 'IMDb评分' in i:
    grade = i[6:]
elif '片  长' in i:
    length = i[5:]
elif '简  介' in i:
    introduction = i[5:]
'''
