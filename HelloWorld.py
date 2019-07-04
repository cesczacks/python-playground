import requests

proxies = {
    'http': 'http://KJ69BG:cescFabregas44@nnlj-kk-prxy-vip.jp.intranet:8080',
    'https': 'http://proxy.jp.intranet:8080'
}

r = requests.get('https://www.douban.com/', proxies=proxies)
print(r.status_code)
print(r.text)
