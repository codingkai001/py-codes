import time
import requests
import re
from bs4 import BeautifulSoup
import pymysql
import threading
import sys

'''
电影资源需求：影片名，发布时间，下载地址，产地，评分，简介，封面图片url。
'''
BASE_URL = 'http://www.dytt8.net'
SUB_SITE_URL = {'rihan': '/html/gndy/rihan/', 'oumei': '/html/gndy/oumei/',
                'dyzz': '/html/gndy/dyzz/', 'china': '/html/gndy/china/',
                'jddy': '/html/gndy/jddy/'}


def sub_site_req(post_url):
    sub_site = BASE_URL + SUB_SITE_URL[post_url] + 'index.html'
    html_code = requests.get(sub_site)
    return html_code.text


def page_url_req(text):
    soup = BeautifulSoup(text, 'html.parser')
    select = soup.find('select', attrs={'name': 'sldd'})
    if select is not None:
        return select


def per_page_req(select_tag):
    soup = BeautifulSoup(str(select_tag), 'html.parser')
    lists = soup.find_all('option')
    for List in lists:
        if re.match('^list_\d+_\d+.html$', List['value']):
            yield List['value']


def movie_url_req(page_url):
    html = requests.get(page_url)
    # html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'html.parser')
    movie_url = soup.find('div', attrs={'class': 'co_content8'})
    # movie_detail_url = BeautifulSoup(movie_url, 'html.parser')
    a_tags = movie_url.find_all('a', attrs={'class': 'ulink'})
    for a in a_tags:
        if re.match('^/html/gndy/[a-z]+/[0-9]+/[0-9]+.html$', a['href']):
            yield a['href']
            # print(a)


def movie_detail_req(movie_url):
    html = requests.get(movie_url)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'html.parser')
    detail = soup.find('div', attrs={'id': 'Zoom'})
    link = detail.find('a')
    img = detail.find('img')
    #  and re.match('^http://www.imageto.org/images/.+', img['src'])
    if img is not None:
        if link is not None and re.match('^ftp://ygdy8:ygdy8.+', link['href']):
            db = pymysql.connect('localhost', 'root', 'fk290419', 'movie', charset='utf8')
            cursor = db.cursor()
            sql = "INSERT IGNORE INTO MOVIE_LIST(LINK,COVER,URL) VALUES ('%s','%s','%s')" \
                  % (str(movie_url), str(img['src']), str(link['href']))
            try:
                cursor.execute(sql)
                db.commit()
                print('数据插入成功。。。')
            except Exception as e:
                print('插入失败。。。', e)
                db.rollback()


if __name__ == '__main__':
    for text, sub_url in zip(map(sub_site_req, SUB_SITE_URL.keys()), SUB_SITE_URL.keys()):
        select_tag = page_url_req(text)
        for page in per_page_req(select_tag):
            page_url = BASE_URL + SUB_SITE_URL[sub_url] + page
            for post_url in movie_url_req(page_url):
                url = BASE_URL + post_url
                movie_detail_req(url)
                time.sleep(1)
