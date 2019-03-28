from flask import Flask,request
from db import db_connent
import re
from setting import INFOURL


app = Flask(__name__)


@app.route('/')
def index():
    return("Welcome To The Token List")

@app.route('/api/count')
def get_count():
    conn = db_connent()
    return str(conn.find().count())


@app.route('/api/all')
def get_all():
    item = []
    conn = db_connent()
    for i in conn.find({},{"_id":0}):
        item.append(i)
    return str(item)       
           
@app.route('/api/symbol/<symbolName>')
def get_symbol(symbolName):
    # symbolName = request.args.get("symbol")
    conn = db_connent()
    symbol = conn.find_one({'symbol':{'$regex': '^'+symbolName+'$', "$options":"i"}},{"_id":0}) 
    return str(symbol)

@app.route('/api/symbol/<symbolName>/info/')
def get_symbol_info(symbolName):
    # symbolName = request.args.get("symbol")
    conn = db_connent()
    symbolID = conn.find_one({'symbol':{'$regex': '^'+symbolName+'$', "$options":"i"}},{'id':1,"_id":0}) 
    return str(INFOURL.format(id=symbolID['id']))

@app.route('/api/name/<Name>/')
def get_name(Name):
    # Name = request.args.get("name")
    conn = db_connent()
    names = conn.find_one({'name':{'$regex': '^'+Name+'$', "$options":"i"}},{"_id":0}) 
    return str(names)

@app.route('/api/name/<Name>/info/')
def get_name_info(Name):
    # Name = request.args.get("name")
    conn = db_connent()
    nameID = conn.find_one({'name':{'$regex': '^'+Name+'$', "$options":"i"}},{'id':1,"_id":0}) 
    return INFOURL.format(id=nameID['id'])


if __name__ == '__main__':
    app.run(debug=True)