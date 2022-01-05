from get import create_table, get_price, get_volume, get_change
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Specify the cryptocurrency symbol")
parser.add_argument("currency", help="Specify the 3 digit currency code")
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know")
args = parser.parse_args()
print(args.crypto, args.currency, args.specific_data)


create_table('btcusd')

print(get_price(), get_volume(), get_change())