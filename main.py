from get import create_table, get_price, get_volume, get_change
import argparse

'''
This is the main file where we created
the interaction between users and the
bitstamp API.
We used argparse module to configure
positional and optional arguments.

There are two positional argument:
crypto and currency which reprepsent
respectively cryptocurrency and currency
selected by the user

Additionally, the user can specify 
which information to display, such as
last price, daily change, volume or
hourly chart
'''

parser = argparse.ArgumentParser()

parser.add_argument("crypto", help = "Specify the cryptocurrency symbol")
parser.add_argument("currency", help = "Specify the 3 digit currency code")
parser.add_argument("-sd","--specific_data", help = "Specify which information you want to know")

args = parser.parse_args()

value = args.crypto + args.currency # Concatenate value for API

create_table(value)

if args.specific_data == "price":
    print("{} value in {} is {}".format(args.crypto, args.currency, get_price()))
elif args.specific_data == "volume":
    print("{} 24h volume is {}".format(args.crypto, get_volume()))
elif args.specific_data == "change":
    print("{} daily change is {} %".format(args.crypto, get_change()))
else:
    print("{} value in {} is {}".format(args.crypto, args.currency, get_price()))
    print("{} 24h volume is {}".format(args.crypto, get_volume()))
    print("{} daily change is {} %".format(args.crypto, get_change()))





















