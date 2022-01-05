from get import create_table, get_price, get_volume, get_change
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("crypto")
parser.add_argument("currency")
parser.add_argument("-sd","--specific_data")
args = parser.parse_args()
print(args.crypto, args.currency, args.specific_data)


create_table('btcusd')

print(get_price(), get_volume(), get_change())