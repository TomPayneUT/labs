import i2c_driver
import yfinance
from time import sleep
import requests

lcd = i2c_driver.LCD()



#How is my RPi going to know the stock prices
company = input('Type a ticker symbol: ')

while True:
    ticker = yfinance.Ticker(company)
    name = ticker.info['symbol']
    price = str(ticker.info['currentPrice'])
    lcd.lcd_display_string(f'{name}: {price}', 1)

    results = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    results = results.json()
    btc_price = results['bpi']['USD']['rate']
    lcd.lcd_display_string(f'BTC: {btc_price}', 2)
    sleep(3)