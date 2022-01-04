# -*- coding: utf-8 -*-
import processingData
from matplotlib import pyplot
import processingData


class DrawTable:
    def __init__(self):
        url = "D:\Files\大数据\整合.csv"
        #self.pyplot = pyplot()
        self.pd = processingData.ProcessingData(url)
        self.pd.showData()
        pyplot.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
        pyplot.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

    def showBar(self):
        areas = ['中山区', '甘井子区', '沙河口区', '高新园区', '西岗区', '旅顺口区', '开发区', '金州区']
        prices = []
        for area in areas:
            prices.append(self.pd.getAverage('所在区域', area))
        pyplot.bar(areas, prices)
        pyplot.title('大连市各地区二手房平均房价')
        pyplot.xlabel('地区')
        pyplot.ylabel('房价/元每平方米')
        return pyplot


    def showScatter(self):
        x = self.pd.getRow('房屋总价')
        y = self.pd.getRow('单价')
        pyplot.scatter(x, y, s=2, marker='.')
        pyplot.title('大连市二手房每平米价格与总价的关系')
        pyplot.xlabel('房屋总价/万元')
        pyplot.ylabel('房价/元每平方米')
        return pyplot

    def showPie(self):
        stataus = ['毛坯','简装','精装','其他']
        num = []
        for i in stataus:
            num.append(self.pd.getNum('装修情况',i))
        pyplot.pie(num ,labels=stataus ,autopct='%1.2f%%')
        pyplot.title('大连市二手房不同装修程度占比')
        return pyplot

    def showBar2(self):
        stataus = ['毛坯','简装','精装','其他']
        prices = []
        for i in stataus:
            prices.append(self.pd.getAverage('装修情况',i))
        pyplot.bar(stataus, prices)
        pyplot.title('大连市二手房不同装修程度平均房价')
        pyplot.xlabel('装修程度')
        pyplot.ylabel('房价/元每平方米')
        return pyplot


