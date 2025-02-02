from get import create_table, get_price, get_volume, get_change
from converter import conversion, convert_table
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
crypto_list = ["btc", "eth", "gbp", "ada" , "xrp", "uni", "ltc", "link", "matic", "xlm", 
                "ftt", "bch", "aave", "axs", "algo", "comp", "snx", "hbar", "chz", "cel", 
                "enj", "bat", "mkr", "zrx", "audio", "skl", "yfi" , "sushi", "alpha", "storj", 
                "sxp", "grt", "uma", "omg", "knc", "crv", "sand", "fet", "rgt", "slp", "eurt", 
                "usdt", "usdc", "dai", "pax", "eth2", "gusd"]

parser.add_argument("crypto", help = "Specify the cryptocurrency symbol", choices = crypto_list)
parser.add_argument("currency", help = "Specify the 3 digit currency code")
parser.add_argument("-sd","--specific_data", help = "Specify which information you want to know",
                choices=["price", "volume", "change"])

args = parser.parse_args()

# By default, the chosen currency is usd
value = args.crypto + "usd"

create_table(value)
"""
If the currency inputted by the user is not usd we created a function to 
convert values (last and open) in order to return the value with the
correct currency
"""

if args.currency != "usd":
    convert_table(args.currency)

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