##Modules
import json
from pprint import pprint
import requests

##Variables
debug = 1
#CoinMarketCap variables
cAPIURL = 'https://api.coinmarketcap.com/v1/ticker/'

#IEX variables
iexAPIURL = 'https://api.iextrading.com/1.0/stock/'

##CoinMarketCap script
#Get JSON data from AV
cCCSymbol = ['bitcoin','bitcoin-cash','ethereum','litecoin','ripple','dash','zcash','monero','stellar','tron','neo','wabi','substratum']
allCurrency = []
for eachCCSymbol in cCCSymbol:
    currency = []
    cFullURL = cAPIURL + eachCCSymbol
    cJSONData = requests.get(cFullURL).json()
    cCurrentPrice = float(cJSONData[0]['price_usd'])
    currency.append(round(cCurrentPrice,2))
    allCurrency.append(currency)

iexSMSymbol = ['znga', 'mck', 'fit']
allStock = []
for eachSMSymbol in iexSMSymbol:
    stock = []
    iexFullURL = iexAPIURL + eachSMSymbol + '/quote'
    iexJSONData = requests.get(iexFullURL).json()
    iexCurrentPrice = float(iexJSONData['latestPrice'])
    stock.append(round(iexCurrentPrice,2))
    allStock.append(stock)

#Print all JSON data for testing
if debug == 0:
    print(allCurrency)
    print(allStock)

#Final variables
stocksCurrenciesOutput = ('\n'.join([
    'var btcPrice = "' + "$ " + str(allCurrency[0][0]) + '";',
    'var btcCashPrice = "' + "$ " + str(allCurrency[1][0]) + '";',
    'var ethPrice = "' + "$ " + str(allCurrency[2][0]) + '";',
    'var ltcPrice = "' + "$ " + str(allCurrency[3][0]) + '";',
    'var ripplePrice = "' + "$ " + str(allCurrency[4][0]) + '";',
    'var dashPrice = "' + "$ " + str(allCurrency[5][0]) + '";',
    'var zcashPrice = "' + "$ " + str(allCurrency[6][0]) + '";',
    'var moneroPrice = "' + "$ " + str(allCurrency[7][0]) + '";',
    'var stellarPrice = "' + "$ " + str(allCurrency[8][0]) + '";',
    'var tronPrice = "' + "$ " + str(allCurrency[9][0]) + '";',
    'var neoPrice = "' + "$ " + str(allCurrency[10][0]) + '";',
    'var wabiPrice = "' + "$ " + str(allCurrency[11][0]) + '";',
    'var substratumPrice = "' + "$ " + str(allCurrency[12][0]) + '";',
    'var zngaPrice = "' + "$ " + str(allStock[0][0]) + '";',
    'var mckPrice = "' + "$ " + str(allStock[1][0]) + '";',
    'var fitPrice = "' + "$ " + str(allStock[2][0]) + '";',
    '\n',
    ]))
