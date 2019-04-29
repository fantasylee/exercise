# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import requests
"""
begain_url='http://www.laifudao.com/tupian/81055.htm'#全站最新的一张gif动图
"""
def run_get_gif(url):
    with open('logging.log','a',encoding='utf-8') as logfile:
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        req = requests.get(url=url, headers=headers, timeout=(3.05, 10))
        req.encoding = 'utf-8'
        html = req.text
        urll = BeautifulSoup(html, 'html.parser')
        filename=urll.title.string.split('_')[0]+'.gif'
        print(filename)
        pic_down_url_ele = urll.find(class_='pic-content') .find('img') # 定位图片的元素位置
        pic_down_url = pic_down_url_ele.get('src')  # 获取图片链接
        next_button_url=urll.findAll('strong')[-1].a.get('href')
        try:
            urllib.request.urlretrieve(url=pic_down_url, filename='D://image4//' + filename)#下载
            print(url,filename,'success',file=logfile)
        except:
            print(url,filename, 'failed',file=logfile)
        next_url = 'http://www.laifudao.com/' + next_button_url
        return next_url

url='http://www.laifudao.com/tupian/42592.htm'
while True:
    try:
        next_url = run_get_gif(url=url)
        url=next_url
    except:
        print('Error')

