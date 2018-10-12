import requests
from bs4 import BeautifulSoup


class FZUJwch:
    index_url = 'http://jwch.fzu.edu.cn/'

    def __int__(self):
        self._user = input('请输入用户名：')
        self._passwd = input('请输入密码：')

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, value):
        self._passwd = value
