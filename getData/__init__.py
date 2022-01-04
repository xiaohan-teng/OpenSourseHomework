
import requests
from bs4 import BeautifulSoup
import mongoConnection
import csv

class Sniper:
    def __init__(self,url):
        self.page = 2
        self.url = url
        url = url + 'pg'+ str(self.page) + '/'
        self.source = requests.get(url)
        self.con = mongoConnection.MongoConnection()
        print(type(self.source))
    def getText(self):
        url = self.url + 'pg' + str(self.page) + '/'
        self.source = requests.get(url)
        return self.source.text
    def getURLs(self):
        text = self.getText()
        soup = BeautifulSoup(text, "html.parser")
        data = soup.select('#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul > li > div > div.title > a')
        print(data)
        result = []
        for i in data:
            result.append(i.get('href'))
        print(result)
        return result
    def getMessage(self,urls):
        for url in urls:
            data = requests.get(url)
            text = data.text
            soup = BeautifulSoup(text, "html.parser")
            data = soup.select('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > div.price > span.total')
            result = []
            result.append('所在区域')
            result.append('普兰店')
            #result = {}
            #result['所在区域'] = '甘井子区'
            result.append('房屋总价')
            price = data[0].text
            result.append(price)
            soup = BeautifulSoup(text, "html.parser")
            data = soup.select('#introduction > div > div > div.base > div.content > ul > li')
            with open("D:\Files\大数据\普兰店.csv", "a", newline="") as cf:
                w = csv.writer(cf)
                for i in data:
                    result.append(i.text[0:4])
                    result.append(i.text[4:])
                    #result[i.text[0:4]] = i.text[4:]
                print(result)
                w.writerow(result)
                cf.close()
        self.page = self.page + 1
