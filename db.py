import pymongo
from setting import DBHOST,DBPORT

def db_connent():
    client = pymongo.MongoClient(host=DBHOST,port=DBPORT)
    db = client['token']
    tokenlist = db['tokenlist']
    return tokenlist

def Save(mess):
    conn = db_connent()
    conn.insert_one(mess)


