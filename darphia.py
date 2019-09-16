import requests
import xlwt
from UA import get_ua
from xsl import save,write_xlwt
from lxml import etree
import re
class Darphia():
    def __init__(self):
        self.start_url = 'https://www.darphin.com/'
        self.headers = {
            'User-Agent': get_ua()
        }

    #  获取以及连接
    def get_page(self):
        page = requests.get(url=self.start_url,headers=self.headers).text
        html = etree.HTML(page)
        res_list = html.xpath('//div[@class="content"]/ul/li/a')
        l = []
        for i in range(2):
            url = 'https://www.darphin.com' + res_list[i].xpath('./@href')[0]
            series = res_list[i].xpath('./@href')[0][1:]
            tup = (url,series)
            l.append(tup)
        return l

    def get_two_page(self):
        l = self.get_page()
        l_all = []
        for i in l:
            url = i[0]
            series = i[1]
            page = requests.get(url,headers=self.headers).text
            html = etree.HTML(page)
            url_list =  html.xpath('//div[@class="product-brief__picture-container"]/a')
            for l in url_list:
                url = l.xpath('./@href')[0]
                tup = (url,series)
                l_all.append(tup)
        return l_all

    def get_three_page(self):
        l = self.get_two_page()
        for i in l:
            url = 'https://www.darphin.com' + i[0]
            # 系列
            series = i[1]
            page = requests.get(url,headers=self.headers).text
            html = etree.HTML(page)
            # 商品中文标题
            if not re.findall(r'<div class="product-full__content">.*?<h1>(.*?)</h1>',page,re.S):
                name = 'N/A'
            else:
                name = re.findall(r'<div class="product-full__content">.*?<h1>(.*?)</h1>',page,re.S)[0]
            # 主图片
            if not re.findall(r'<div class="spp-sticky-add-to-bag__image-single">.*?lazyload" data-src="(.*?)" alt="" '
                              r'/>',page,re.S):
                img = 'N/A'
            else:
                img_list = re.findall(r'<div class="spp-sticky-add-to-bag__image-single">.*?lazyload" data-src="(.*?)" alt="" '
                              r'/>',page,re.S)
                s = set(img_list)
                img_list = list(s)
                img = ''
                for i in img_list:
                    img += 'https://www.darphin.com'+ i + ' ' + '|'
            # 价格
            if not re.findall(r'<option class="sku-menu__option".*?>(.*?)</option>',page,re.S):
                price = 'N/A'
            else:
                price_list = re.findall(r'<option class="sku-menu__option".*?>(.*?)</option>',page,re.S)
                l = []
                for i in price_list:
                    i.replace("\n","")
                    i.strip()
                    l.append(i)
                s = set(l)
                price_l = list(s)
                print(price_l)

            #print(price)






















    def main(self):
        self.get_three_page()

if __name__ == '__main__':
    spider = Darphia()
    spider.main()
