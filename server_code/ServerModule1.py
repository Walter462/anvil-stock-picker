import anvil.secrets
import anvil.server
import requests 

# GitHub as MD link
# | NOTE: Securely setting FinnHub API as constant  | File: KnowlegeBase/IT/Development/DataDrivenApps/Anvil/Tutorials/StockPicker | ID: 1733641711 |
FINNHUB_KEY = anvil.secrets.get_secret("FinnHubAPI")
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

# | NOTE: Hardcoded stock names for dropdown menu | File: KnowlegeBase/IT/Development/DataDrivenApps/Anvil/Tutorials/StockPicker | ID: 1733644314 |
@anvil.server.callable
def getTickers():
  tickers =['AAPL', 'TSLA', 'GME', 'AMC']
  return(tickers)

# | NOTE: External API call | File: KnowlegeBase/IT/Development/DataDrivenApps/Anvil/Tutorials/StockPicker | ID: 1733642894 |
@anvil.server.callable
def getPrice(ticker):
  r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={FINNHUB_KEY}')
  price = r.json()['c']
  return(price)