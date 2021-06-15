import requests as req
from bs4 import BeautifulSoup as bs

import pandas as pd
import datetime




def scrap_data():
    
    url='https://coinmarketcap.com/currencies/bitcoin/historical-data/'
    
    df=pd.read_csv('../data/bth_price.csv')

    html=req.get(url, 'html.parser').content

    soup=bs(html)

    bitcoin_price=soup.find('div', class_='priceValue___11gHJ').text

    bitcoin_price_var=soup.find('span', class_='sc-15yy2pl-0 gEePkg').text

    bit_eth_price=soup.find('p', class_='esfl2f-0 kqzSsi').text.split('H')[0]+'H'

    bit_eth_price_var=soup.find('p', class_='esfl2f-0 kqzSsi').text.split('H')[1]



    dictio={'bitcoin_price': bitcoin_price,
           'bitcoin_price_var': bitcoin_price_var,
           'bit_eth_price': bit_eth_price,
           'bit_eth_price_var': bit_eth_price_var,
           'datetime': datetime.datetime.now()}


    df=df.append(pd.DataFrame(dictio, index=[0]), ignore_index=True)

    df.to_csv('../data/bth_price.csv', index=False)

    return df.shape





def clean_data():

    df=pd.read_csv('../data/bth_price.csv')

    try:

        df.bitcoin_price=df.bitcoin_price.apply(lambda x: float(x.replace('$', '').replace(',', '')))

        df.bitcoin_price_var=df.bitcoin_price_var.apply(lambda x: float(x.replace('%', '')))

        df.bit_eth_price=df.bit_eth_price.apply(lambda x: float(x.replace('ETH', '')))

        df.bit_eth_price_var=df.bit_eth_price_var.apply(lambda x: float(x.replace('%', '')))

    except:
        print('Data ya esta limpia')

    df=df.dropna()
    df.to_csv('../data/bth_price.csv', index=False)

    return df.shape


