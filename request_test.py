
import requests

url = 'http://onlineclock.net/images/menu.png'

headers = {
    'accept-ranges': 'bytes',
    'age': '1314977',
    'alt-svc': 'h3-27=":443"; ma=86400, h3-28=":443"; ma=86400, h3-29=":443"; ma=86400, h3=":443"; ma=86400',
    'cache-control': 'max-age=31536000',
    'cf-bgj': 'imgq:85,h2pri',
    'cf-cache-status': 'HIT',
    'cf-polished': 'origFmt=png, origSize=265',
    'cf-ray': '66830e60caec1710-SIN',
    'content-disposition': 'inline; filename="menu.webp"',
    'content-length': '128',
    'content-type': 'image/webp',
    'date': 'Thu, 01 Jul 2021 22:26:28 GMT',
    'expect-ct': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
    'last-modified': 'Sun, 11 Jun 2017 13:47:06 GMT',
    'server': 'cloudflare',
    'vary': 'Accept',
    'x-cache-info': 'caching',
    'x-content-type-options': 'nosniff',
    'x-xss-protection': '1; mode=block',
}

proxy = {
    'https': '127.0.0.1:4780'
}

file_name = '001'

response = requests.get(url, headers=headers, proxies=proxy)
with open(f'./{file_name}', 'wb') as f:  # /为分级 wb代表二进制模式文件，允许写入文件，
    f.write(response.content)

