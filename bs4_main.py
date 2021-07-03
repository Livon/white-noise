import re

import requests
from bs4 import BeautifulSoup

"""
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
"""
soup = BeautifulSoup(open('main.html'), features='html.parser')  # html.parser是解析器，也可是lxml

print(f'抽取title：{soup.title}')
print(f'抽取图片：{soup.img}')

proxy = {
    'https': '127.0.0.1:4780'
}

print('- links - - - - - - - - - - ')
links = soup.find_all('link')
for source in links:
    print(f"http:{source['href']}")

print('- scripts - - - - - - - - - - ')
scripts = soup.find_all('script', attrs={'src': True})
for script in scripts:

    if re.match('http', script['src']):
        print(script['src'])
    if re.match('//', script['src']):
        print(f"http:{script['src']}")


print('- sources - - - - - - - - - - ')
sources = soup.find_all('source')
for source in sources:
    # print(source['src'])
    print(f"http:{source['src']}")

imgs = soup.find_all('img')
for img in imgs:
    # print(type(img))
    print(img['src'])

    url = ''
    if re.match('//', img['src']):
        # print(re.match('//', img['src']).span())  # 在起始位置匹配
        url = f"http:{img['src']}"
        print(url)  #
    else:
        url = f"https://onlineclock.net/noisegenerator/{img['src']}"
        print(url)  #

    # save_to = ''
    # if re.search('numerals', img['src']):
    #     save_to = 'numerals'
    # if re.search('images', img['src']):
    #     save_to = 'images'
    #
    # file_name = img['src'].split('/')[-1]  # 以/为分隔符，取最后一段作为文件名
    #
    # headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    #
    # response = requests.get(url, headers=headers, proxies=proxy)
    # with open(f'./{save_to}/{file_name}', 'wb') as f:  # /为分级 wb代表二进制模式文件，允许写入文件，
    #     f.write(response.content)
# ————————————————
# 版权声明：本文为CSDN博主「饿了就点外卖」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / weixin_50990952 / article / details / 111796512
