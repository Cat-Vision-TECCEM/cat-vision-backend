import random

import pandas as pd
COMPANY = 'Company'
STORE = 'Store'
PRODUCTS = pd.read_csv('products.csv')

NUMBER_OF_COMPANIES = 10
NUMBER_OF_STORES = 15

def sendRequest(url, jason):
    import requests
    import json
    headers = {'Content-type': 'application/json'}


    x = requests.post(url, json.dumps(jason), headers=headers)

    print(x.text)

# CREATE COMPANIES
companies_list = []
for i in range(0,NUMBER_OF_COMPANIES):
    url = 'http://127.0.0.1:8080/company/create'
    json = {
        'name': COMPANY + str(i),
        'email': f'hola@{(COMPANY+str(i)).lower()}.com'
    }
    companies_list.append(json)
    sendRequest(url, json)

# CREATE STORES
stores_list = []
for i in range(0,NUMBER_OF_STORES):
    url = 'http://127.0.0.1:8080/store/create'
    json = {
        'name': STORE + str(i),
        'street': f'Street{i}',
        'state': f'State{i}',
        'number': f'#{i}',
        'city': f'City{i}',
        'password': '1234567890'
    }
    stores_list.append(json)
    sendRequest(url, json)

# CREATE PRODUCTS
products_list = []

for i in range(0,PRODUCTS.shape[0]):
    url = 'http://127.0.0.1:8080/product/create'
    json = {
        'company_id': random.choice(companies_list),
        'sku': PRODUCTS.iloc[i]['sku'],
        'name':PRODUCTS.iloc[i]['name'],
        'selling_price':PRODUCTS.iloc[i]['selling_price'],
        'image':PRODUCTS.iloc[i]['image']
    }
    products_list.append(json)
    sendRequest(url, json)


"""# CREATE COMPANY_STORE
for i in range(0, NUMBER_OF_COMPANIES):
    url = """