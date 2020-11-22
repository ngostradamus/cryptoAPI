  
 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol':'ETH'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'paste API key here',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
  parseData = json.dumps(response.json())
  #print(parseData)
  ethObj = json.loads(parseData)
  print(ethObj["data"]["ETH"]["name"])
  print(ethObj["data"]["ETH"]["quote"]["USD"]["price"])

  ethString = str(ethObj["data"]["ETH"]["quote"]["USD"]["price"])
  ethPrice = float(ethString)

  if(ethPrice > 500):
    print("I'm filthy rich!")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
