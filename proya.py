import requests
from lxml import etree
from UA import get_ua
from xsl import write_xlwt,save
import xlwt
class Proya():
    def __init__(self):
        self.header ={'User-Agent':get_ua()}
        self.url = 'https://www.proya.com/'
    def get_page(self):
        page1 = requests.get('https://www.proya.com/about/',headers = self.header).text
        html1 = etree.HTML(page1)
        # 描述
        describe = html1.xpath('//div[@class="w1200"]/div[@class="tits"]/text()')[0]
        # 品牌故事
        story = ''
        for i in html1.xpath('//div[@class="w1200"]/div[@class="txt"]/text()'):
            story += i
        page = requests.get(self.url,headers=self.header).text
        html = etree.HTML(page)
        type_list = html.xpath('//li[@class="li"]')
        # 官网链接
        url = self.url
        l = []
        for type in type_list:
            # 分类
            classify = type.xpath('./a/text()')[0]
            series_lsit = type.xpath('.//div[@class="cnav f-cb"]/dl/dd/a')
            for series in series_lsit:
                series_url = 'https://www.proya.com/'+ series.xpath('./@href')[0]
                # 系列
                if '/' in series.xpath('./text()')[0]:
                    series = series.xpath('./text()')[0]
                    series = series.replace('/','-')
                else:
                    series = series.xpath('./text()')[0]
                lis = [describe,story,classify,series,series_url,url]
                l.append(lis)
        print(l)
        return l
    def get_two_page(self):
        l = self.get_page()
        l_t = []
        for i in l:
            describe,story,classify,series,series_url,url = i[0],i[1],i[2],i[3],i[4],i[5]

            # print(classify, series, series_url)
            page = requests.get(series_url,headers=self.header).text
            html = etree.HTML(page)
            res_list = html.xpath('//ul[@class="f-cb"]/li')
            for res in res_list:
                res_url = 'https://www.proya.com'+res.xpath('./a/@href')[0]
                l1 = (describe,story,classify,series,url,res_url)
                l_t.append(l1)

        return l_t
    def get_three_page(self):
        l = self.get_two_page()
        l_all = []
        for i in l:
            describe,story,classify,series,url,res_url = i[0],i[1],i[2],i[3],i[4],i[5]
            page = requests.get(res_url,headers=self.header).text
            html = etree.HTML(page)
            # 商品标题
            if not html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@alt'):
                name = 'N/A'
            else:
                if '/' in html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@alt')[0]:
                    name = html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@alt')[0]
                    name = name.replace('/','-')
                else:
                    name = html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@alt')[0]
            # 大图
            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/img/@src'):
                img1 = ''
            else:
                img1 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/img/@src')[0]
            if not html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@src'):
                img2 = ''
            else:
                img2 = html.xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div[2]/img/@src')[0]
            img = 'https://www.proya.com'+img1 + '|' + 'https://www.proya.com' + img2
            # 主要功效
            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[1]/text()'):
                efficacy = 'N/A'
            else:
                efficacy = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[1]/text()')[0]
            # 小图
            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img'):
                simg1 = ''
                scontent1 = ''
            else:
                simg1 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img/@src')[0]
                scontent1 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img/@alt')[0]

            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img'):
                simg2 = ''
                scontent2 = ''
            else:
                simg2 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img/@src')[0]
                scontent2 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/img/@alt')[0]
            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div/img'):
                simg3 = ''
                scontent3 = ''
            else:
                simg3 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div/img/@src')[0]
                scontent3 = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div/img/@alt')[0]
            simg = 'https://www.proya.com' + simg1 + scontent1 + '|' + 'https://www.proya.com' + simg2+ scontent2+'|'+ 'https://www.proya.com' + simg3+scontent3

            # 规格
            if not html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[4]/a'):
                 specifications = 'N/A'
            else:
                specifications = html.xpath('/html/body/div/div[3]/div[1]/div[3]/div[2]/div/div/div[4]/a/text()')[0]
            # 价格
            if not html.xpath('//div[@class="price f-cb"]/i'):
                price = 'N/A'
            else:
                price = html.xpath('//div[@class="price f-cb"]/i/text()')[0]

            # 产品宣称
            if not html.xpath('//div[@class="box1"]/div[@class="txt"]/p/text()'):
                claim = 'N/A'
            else:
                claim_list = html.xpath('//div[@class="box1"]/div[@class="txt"]/p/text()')
                claim = ''
                for i in claim_list:
                    claim += i
            # 使用方法
            if not html.xpath('//div[@class="picList"]/p/text()'):
                usage = 'N/A'
            else:
                usage = html.xpath('//div[@class="picList"]/p/text()')[0]

            # logo
            if not html.xpath('//div[@class="header-m"]/a/img'):
                logo = 'N/A'
            else:
                logo = 'https://www.proya.com' + html.xpath('//div[@class="header-m"]/a/img/@src')[0]
            if not html.xpath('//div[@class="color f-cb"]/div/div/img'):
                model = 'N/A'
            else:
                model = ''
                png = html.xpath('//div[@class="color f-cb"]/div/div/img/@src')
                color = html.xpath('//div[@class="color f-cb"]/div/div/div/i/text()')
                for i, j in zip(png, color):
                    model += 'https://www.proya.com' + i + '--' + j

            tup = (describe,story,classify,series,url,name, img, efficacy, simg, specifications, price, claim, usage,
                   logo, res_url,model)
            print(tup)
                    # 描述, 品牌故事,分类,    系列 ,官网链接,中文标题,大图,主要功效,小图, 规格 , 价格 ,产品宣称,使用方法,logo,产品链接
            l_all.append(tup)
        return l_all

    def write_x(self):
        count = 0
        l = self.get_three_page()
        for i in l:
            describe, story, classify, series, url, name, img, efficacy, simg, specifications, price, claim, usage,\
            logo, res_url,model = i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15]
            xls = xlwt.Workbook(encoding='utf-8')
            ws = xls.add_sheet('Sheet1')
            write_xlwt(ws)
            ws.write(4,4,describe)
            ws.write(8,4,story)
            ws.write(5,1,classify)
            ws.write(4,1,series)
            ws.write(5,4,url)
            ws.write(2,1,name)
            ws.write(9,1,img)
            ws.write(17,1,efficacy)
            ws.write(10,1,simg)
            ws.write(7,1,specifications)
            ws.write(8,1,price)
            ws.write(11,1,claim)
            ws.write(13,1,usage)
            ws.write(3,4,logo)
            ws.write(19,1,res_url)
            ws.write(6,1,model)
            save(xls, series + '-' + name)
            count+=1
            print('成功',count)


    def main(self):
        self.write_x()

if __name__ == '__main__':
    s = Proya()
    s.main()













