import json
import requests

api_url_base = 'https://api.quotable.io'

response = requests.get(api_url_base)
if(response.status_code == 200):
    print('Quotable API Connected!')

def get_quote():
    quote = requests.get(api_url_base + '/random')
    quote_json = quote.json()

    # _id, tags, content, author, length
    return('{} \n\t- {}'.format(quote_json['content'], quote_json['author']))
