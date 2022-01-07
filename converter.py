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