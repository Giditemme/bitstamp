import pandas as pd
from currency_converter import CurrencyConverter

def conversion(price, default_currency, output_currency):
	
    '''
    This function convert values from the original 
    currency to the currency specified by the user
    '''
    c = CurrencyConverter()
    default_currency = default_currency.upper() 
    output_currency = output_currency.upper()
    converted_price = c.convert(price, default_currency, output_currency)
    return converted_price

def convert_table(output_currency):
    '''
    This function uses the conversion function
    to convert values such as opening price and 
    last price
    '''
    df = pd.read_csv('CryptoTable.csv')
    df['last'] = conversion(df._get_value(0, 'last'), "usd", output_currency)
    df['open'] = conversion(df._get_value(0, 'open'), "usd", output_currency)
    df.to_csv (r'CryptoTable.csv', index = False, header=True)
