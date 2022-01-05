import requests
import json
import pandas as pd


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'


def create_table(value):

    '''
    This function creates a csv file to fetch 
    data from bitstamp API and store it in a table
    '''
    r = requests.get(bitstamp_URL % value)
    file_json = json.loads(r.text)
    df = pd.DataFrame(file_json, index=[0])
    df.to_csv (r'CryptoTable.csv', index = False, header=True)

def get_price():

    '''
    This function returns the variable last_price, 
    which is the last price of the cryptocurrency selected
    '''
    df = pd.read_csv('CryptoTable.csv')
    last_price = df._get_value(0, 'last')
    return last_price


def get_volume():

    '''
    This function returns the  volume which is the daily 
    volume of the cryptocurrency selected
    '''

    df = pd.read_csv('CryptoTable.csv')
    volume = df._get_value(0, 'volume')
    return volume


def get_change():

    '''
    This function calculate the change in price based on 
    the opening and last price available for the 
    cryptocurrency
    '''

    df = pd.read_csv('CryptoTable.csv')
    open_price = df._get_value(0, 'open')
    last_price = df._get_value(0, 'last')
    return (last_price-open_price)/last_price*1004
