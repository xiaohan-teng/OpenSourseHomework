from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
sc = SparkContext()
ctx = SQLContext(sc)
test_collection = ctx.read.format("com.mongodb.spark.sql").options(uri="mongodb://192.168.0.1:27017", database="test_db", collection="test_collection").load()
test_collection.printSchema()
test_collection.first()
test_collection.registerTempTable("houses")
sql = "select * from houses where area = 'ÖÐÉ½Çø'"
result = ctx.sql(sql)
est_rdd = test_collection.rdd
result.write.format("com.mongodb.spark.sql").mode("overwrite").options(uri="mongodb://192.168.0.1:27017", database="test_db", collection="test_collection_out").load()
fields_list = "name age sex grade exp"
fields = [StructField(field_name, StringType(), True) for field_name in fields_list]
schema = StructType(fields)
df = ctx.createDataFrame(result, schema=schema)
df.write.format("com.mongodb.spark.sql").mode("overwrite").options(uri="mongodb://192.168.0.1:27017", database="test_db", collection="test_collection_out").load()