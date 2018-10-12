import requests
from bs4 import BeautifulSoup

url = "http://www.epubit.com.cn/tag/details/12"
http = requests.get(url)
l = BeautifulSoup(http.text, "html.parser")
booklist = l.find_all('p', attrs={"class": "bookList__summary"})
for i in booklist:
    print(i.text.strip())
