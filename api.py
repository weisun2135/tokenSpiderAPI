from flask import Flask,request
import pymongo
import re



app = Flask(__name__)
def get_list():
    client = pymongo.MongoClient(host='47.244.154.170',port=27017)
    db = client['token']
    tokenlist = db['tokenlist']
    return tokenlist

@app.route('/')
def index():
    return("Welcome to the token list")

@app.route('/api/count')
def get_count():
    conn = get_list()
    return str(conn.find().count())


@app.route('/api/all')
def get_all():
    item = []
    conn = get_list()
    for i in conn.find({},{"_id":0}):
        item.append(i)
    return str(item)       
           
@app.route('/api/symbol')
def get_symbol():
    symbolName = request.args.get("symbol")
    conn = get_list()
    symbol = conn.find_one({'symbol':{'$regex': '^'+symbolName+'$', "$options":"i"}}) 
    return str(symbol)
@app.route('/api/name/')
def get_name():
    Name = request.args.get("name")
    conn = get_list()
    names = conn.find_one({'name':{'$regex': '^'+Name+'$', "$options":"i"}}) 
    return str(names)


if __name__ == '__main__':
    app.run(debug=True)