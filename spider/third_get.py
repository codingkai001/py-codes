import requests


# 利用字典抓取
urls_dict = {
    '电子工业出版社': 'http://www.phei.com.cn',
    '在线资源': 'http://phei.com.cn/module/zygl/zxzyindex.jsp',
    '百度': 'www.baidu.com',  # 抛出异常
    '网上书店1': 'http://phei.com.cn/module/goods/wssd_index.jsp',  # 去重测试
    '网上书店2': 'http://phei.com.cn/module/goods/wssd_index.jsp'
}

crawled_urls_for_dict = set()   # 空集合
for index, name in enumerate(urls_dict.keys(), 1):     # 返回键的索引和键组成的元组,索引从1开始
    name_url = urls_dict[name]
    if name_url in crawled_urls_for_dict:
        print("[%s] 已经抓取过了！" % name_url)
    else:
        try:
            resp = requests.get(name_url)
        except Exception as e:
            print("抓取异常：", index, name, ':', str(e), sep='')     # 输出抓取异常的名称和异常信息
            continue

        content = resp.text
        crawled_urls_for_dict.add(name_url)     # 将已抓取的url添加到集合中
        with open('bydict_'+name+'.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print("抓取完成：{}{},大小为{}KB".format(index, name, len(content)//1024))







