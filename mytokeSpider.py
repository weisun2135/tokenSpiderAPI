from urllib.parse import urlencode
import requests
import time
import redis


def get_page(page):
    params = {

        'page': page,
        'size': '50',
        'subject': 'market_cap',
        'timestamp': '1551959322743',
        'code': 'd0ab5dfef1e2b6a1163d0f6e7249128b',
        'platform': 'web_pc',
        'v': '1.0.0',
        'language': 'zh_CN',
        'legal_currency': 'CNY',
    }
    url = 'https://speed-api.mytokenapi.com/ticker/currencylist?' + urlencode(params)
    # print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
def get_items(json):
    if json.get('data'):
        for item in json['data']['list']:

            yield{
                'id':item['id'],
                'currency_id':item['currency_id'],
                'rank':item['rank'],
                'name':item['name'],
                'symbol':item['symbol'],
                'price':item['price'],
                'price_usd':item['price_usd'],
            }
def radisSave(mess):
    try:
        pool = redis.ConnectionPool(host='47.244.154.170', port=6379, db=mytoken, password='qwe123')
        print("connected success.")
    except:
        print("could not connect to redis.")
    r = redis.StrictRedis(connection_pool=pool)
    r.hset(mess)



def main(page):
    json = get_page(page)
    # print(type(json))
    # btc=json['data']['list'][0]
    # print(type(btc))
    for mess in get_items(json):
        print(mess)

        radisSave(mess)

START=1
END=92
if __name__ == '__main__':
    for i in range(START,END+1):
        # print(i)
        main(i)
        time.sleep(1)