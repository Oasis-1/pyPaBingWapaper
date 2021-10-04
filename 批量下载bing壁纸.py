import time
import urllib.request
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
def down(page):
    url=f"https://bing.ioliu.cn/ranking?p={page}"
    response=requests.get(url=url,headers=headers)
    content=response.content
    tree=etree.HTML(content)
    res=tree.xpath('//img[@class="progressive__img progressive--not-loaded"]/@data-progressive')
    name_list=tree.xpath('//h3/text()')
    for i in range(len(res)):
        res[i]=res[i].replace('_640x480','_1920x1080')
        urllib.request.urlretrieve(url=res[i], filename=str(name_list[i]).split('/')[0]+'.jpg')
        print(name_list[i])
    print(f"第{page}页已完成")
if __name__ == '__main__':
    print("批量下载bing（https://cn.bing.com/）的壁纸（https://bing.ioliu.cn/ranking）")
    start=int(input('起始页'))
    end=int(input('终止页'))
    for i in range(start,end+1):
        down(i)
        print('\n')
    print('下载完成，程序将在3秒后关闭')
    time.sleep(1)
    print('下载完成，程序将在2秒后关闭')
    time.sleep(1)
    print('下载完成，程序将在1秒后关闭')
    time.sleep(1)
