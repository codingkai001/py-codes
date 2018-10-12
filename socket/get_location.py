"""使用谷歌地理编码API获取地址的经纬度"""
import requests
import http.client
import json
from urllib.parse import quote_plus


def geocode1(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'])


def geocode2(address):
    base = '/maps/api/geocode/json'
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    conn = http.client.HTTPConnection('maps.google.com')
    conn.request('GET', path)
    raw_reply = conn.getresponse().read()
    reply = json.loads(raw_reply.decode('utf-8'))
    print(reply['results'])


if __name__ == '__main__':
    geocode1('207 N. Defiance St, Archbold, OH')
