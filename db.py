import pymongo

try:
    client = pymongo.MongoClient(host='47.244.154.170',port=27017)
    db = client['token']
# except pymongo.errors as e:
#     return("连接异常!",e)
