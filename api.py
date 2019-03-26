from flask import Flask,request
from db import db_connent
import re



app = Flask(__name__)


@app.route('/')
def index():
    return("Welcome to the token list")

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
           
@app.route('/api/symbol')
def get_symbol():
    symbolName = request.args.get("symbol")
    conn = db_connent()
    symbol = conn.find_one({'symbol':{'$regex': '^'+symbolName+'$', "$options":"i"}}) 
    return str(symbol)
@app.route('/api/name/')
def get_name():
    Name = request.args.get("name")
    conn = db_connent()
    names = conn.find_one({'name':{'$regex': '^'+Name+'$', "$options":"i"}}) 
    return str(names)


if __name__ == '__main__':
    app.run(debug=True)