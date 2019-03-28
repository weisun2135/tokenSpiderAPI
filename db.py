import pymongo
from setting import DBHOST,DBPORT

def db_connent():
    client = pymongo.MongoClient(host=DBHOST,port=DBPORT)
    db = client['token']
    tokenlist = db['tokenlist']
    return tokenlist

def Find_id(id):
    conn = db_connent()
    try:
        return conn.find_one({'id':id},{'id':1,'_id':0})['id']
       
    except:
        return False
       
def Find_all_id():
    conn = db_connent()
    return conn.find({},{'id':1,'_id':0})


def Update(id,mess):
    conn = db_connent()
    conn.update_one({'id':id},{'$set':{'rank':mess['rank'],'price':mess['price'],'price_usd':mess['price_usd']}})


def Save(mess):
    conn = db_connent()
    conn.insert_one(mess)


# if __name__ == '__main__':
#     for i in Find_all_id():
#         print(i)
#     mess = {
#     "id" : 49653,
#     "currency_id" : 1,
#     "rank" : 1,
#     "name" : "Bitcoin",
#     "symbol" : "BTC",
#     "price" : 26,
#     "price_usd" : 33}
#     Update(mess['id'],mess)