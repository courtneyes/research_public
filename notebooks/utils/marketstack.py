import requests
import json
import pandas as pd
from datetime import date

TODAY = date.today().strftime("%Y-%m-%d")

def get_pricing(ticker, field='all', start_date='2008-01-01', end_date=TODAY):     
    params = { 
        'access_key': '23e7a4b793ea07e119cd8c02e9f869cc',
        'symbols': ticker,
        'date_from': start_date,
        'date_to': end_date,
        'limit': 1000
    }
    
    request = requests.get('http://api.marketstack.com/v1/eod', params)


    try:
        response = request.json()
        data = response['data']
        
        df = pd.DataFrame(data)
        df.set_index('date', inplace=True)
            
        if field == 'all':        
            return df
        
        return df[field]
        
    except:
        print(response['error'])   