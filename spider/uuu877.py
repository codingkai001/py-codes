import requests
from bs4 import BeautifulSoup
import os
import re
import time

url = 'http://www.tsinghua.edu.cn/'
html = requests.get(url)
bs = BeautifulSoup(html.text, "html.parser")
print(html.text)
