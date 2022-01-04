# -*- coding: utf-8 -*-

import pandas
class ProcessingData:
    def __init__(self, url):
        self.url = url
        self.data = pandas.read_csv(url)

    def showData(self):
        print(self.data)

    def getAverage(self ,row ,key):
        total = 0
        length = 0
        for i in range(len(self.data)):
            if self.data[i:i + 1].get(row)[i] == key:
                total += self.data[i:i + 1].get('单价')[i]
                length = length + 1
        print(total / length)
        return total / length

    def getRow(self ,key):
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i:i + 1].get(key)[i])
        return result

    def getNum(self ,row ,key):
        total = 0
        for i in range(len(self.data)):
            if self.data[i:i + 1].get(row)[i] == key:
                total = total + 1
        return total

