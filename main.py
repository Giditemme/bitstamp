from get import create_table, get_price, get_volume, get_change
from converter import conversion

create_table('btcusd')

print(get_price(), get_volume(), get_change())