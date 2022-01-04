from pymongo import MongoClient

class MongoConnection:
    def __init__(self,dbName = 'test',colName = 'newCollection'):
        self.client = MongoClient('127.0.0.1', 27017)#连接
        print(self.client)
        self.db = self.client[dbName];#选择数据库
        print(self.db)
        self.col = self.db[colName]#选择使用集合
        print(self.col)
    '''
    返回当前连接的集合中所有的内容
    返回一个列表，列表中包含集合中的所有文档，文档以字典类型储存
    '''
    def find(self):
        documents = self.col.find()
        result = []
        for document in documents:
            document.pop('_id')#从获取的结果中将用来表达特殊含义的_id从搜索结果中删除
            result.append(document)
        print(result)
        return result
    '''
    在当前集合的所有文档中查找key对应的内容
    可以用来查找房产的价格等
    返回一个列表，列表中包含所有查找结果 没找到的文档中为None
    '''
    def search(self,key):
        result = []
        toSearch = self.find()
        for each in toSearch:
            result.append(each.get(key))
        print(result)
        return result
    '''
    创建一个新的集合（未测试）
    '''
    def createCol(self,colName):
        self.db.create_collection(colName)
    '''
    使用集合（未测试）
    '''
    def useCol(self,colName):
        self.col = self.db[colName]
    '''
    删除集合（未测试）
    '''
    def dropCol(self,colName):
        self.db.drop_collection(colName)
    '''
    插入单个文档
    '''
    def insertOne(self,doc):
        self.col.insert_one(doc)
    '''
    插入多个文档（未测试）
    '''
    def insertMany(self,docs):
        self.col.insert_many(docs)
    '''
    删除一个文档
    参数为字典类型
    '''
    def deleteOne(self,key):
        self.col.delete_one(key)
    '''
    删除多个文档（未测试）
    参数为字典类型
    '''
    def deleteMany(self,key):
        self.col.delete_many(key)

