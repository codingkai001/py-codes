from bs4 import BeautifulSoup
import requests

file = open('book.txt', 'w', encoding='utf-8')
url = 'http://book.dangdang.com/01.54.htm'
book_url = requests.get(url)
bs = BeautifulSoup(book_url.text, 'html.parser')
a_lst = bs.find_all('a')
for a in a_lst:
    if a.text != '' and 'http://product.dangdang.com/' in a['href']:
        file.write(a.text.strip() + '----' + a['href'] + '\n')
file.close()
