import requests
import datetime

api_key = "A0H0JU33VNH5SM02"
base_url = "https://www.alphavantage.co/query?"

# function for currency conversion
def currency_converter(from_value, to_value):
    try:
        print("Doing the conversions....")
        url = base_url + f"function=CURRENCY_EXCHANGE_RATE&from_currency={from_value}&to_currency={to_value}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return exchange_rate
    except KeyError:
        print("Error: Invalid currency code")

# function for Historical data
def historical_data(from_value, to_value):
    try:
        print("Getting the data for you....")
        url = base_url + f"function=FX_DAILY&from_symbol={from_value}&to_symbol={to_value}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        for i in range(5):
            date = str(datetime.date.today() - datetime.timedelta(days=i))
            if date in data['Time Series FX (Daily)']:
                rate = data['Time Series FX (Daily)'][date]['4. close']
                print(f'{date}: {rate}')
            else:
                print(f"No historical data available for {date}")
        print("Done!")
    except KeyError:
        print("Error: Invalid currency code ")

print("__________LIVE CURRENCY CONVERTER__________")
print("Convert the desired amount into any foreign currency! For BitCoin, use the code BTC")
amount = float(input("Enter the amount: "))
from_curr = input("From: ").upper()
to_curr = input("To: ").upper()

exchange_rate = currency_converter(from_curr, to_curr)
if exchange_rate is not None:
    print("The converted amount is: ", amount*exchange_rate)
    print("The exchange rate is: ", exchange_rate)

    # Last 5 days historical data for the same conversion
    menu_cmd = input("Press H and enter to get the last 5 days historical data for the same conversion: ").upper()
    if menu_cmd == 'H':
        historical_data(from_curr, to_curr)
print("Press Enter to exit")
input()
