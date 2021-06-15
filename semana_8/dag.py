import requests as req
from bs4 import BeautifulSoup as bs

import pandas as pd

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def get_bth_price():

    df=pd.read_csv('../data/bth_price.csv')

    html=req.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/', 'html.parser').content

    soup=bs(html)

    bitcoin_price=soup.find('div', class_='priceValue___11gHJ').text

    bitcoin_price_var=soup.find('span', class_='sc-1v2ivon-0 iQVSWO').text

    bit_eth_price=soup.find('p', class_='sc-10nusm4-0 bspaAT').text.split('H')[0]+'H'

    bit_eth_price_var=soup.find('p', class_='sc-10nusm4-0 bspaAT').text.split('H')[1]

    dictio={'bitcoin_price': bitcoin_price,
            'bitcoin_price_var': bitcoin_price_var,
            'bit_eth_price': bit_eth_price,
            'bit_eth_price_var': bit_eth_price_var,
            'datetime': datetime.now()}

    df=df.append(pd.DataFrame(dictio, index=[0]), ignore_index=True)

    df.to_csv('../data/bth_price.csv', index=False)
    
    return 'Get data process DONE'

    
    
def clean_bth_data():
    
    df=pd.read_csv('../data/bth_price.csv')
    try:
        df.bitcoin_price=df.bitcoin_price.apply(lambda x: float(x.replace('$', '').replace(',', '')))
        df.bitcoin_price_var=df.bitcoin_price_var.apply(lambda x: float(x.replace('%', '')))
        df.bit_eth_price=df.bit_eth_price.apply(lambda x: float(x.replace('ETH', '')))
        df.bit_eth_price_var=df.bit_eth_price_var.apply(lambda x: float(x.replace('%', '')))

    except:
        print('Data is clean')

    df.to_csv('../data/bth_price.csv', index=False)

    return 'Clean data process DONE'
    



default_args = {
    'owner': 'yona',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 8),
    'email': ['yehonaga@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'email_on_success': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'bth_scrap',
    description='Bitcoin price scraping',
    schedule_interval='*/1 * * * *',   # cada 1 minuto (https://en.wikipedia.org/wiki/Cron#CRON_expression)
    default_args=default_args,
    catchup=False,
)


tarea1=PythonOperator(task_id='get_bth_price', python_callable=get_bth_price, dag=dag)

tarea2=PythonOperator(task_id='clean_bth_data', python_callable=clean_bth_data, dag=dag)

# secuencia de tareas
tarea1 >> tarea2

# equivalente
#tarea2.set_upstream(tarea1)

