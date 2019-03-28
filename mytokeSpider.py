from urllib.parse import urlencode
from request_get import get_url_json
from setting import START,END,URL

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
    url = URL + urlencode(params)
    # print(url)
    return get_url_json(url)


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




