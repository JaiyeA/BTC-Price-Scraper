import urllib.request
from bs4 import BeautifulSoup
import urllib.error

url= 'https://cointelegraph.com/bitcoin-price-index'
page= urllib.request.urlopen(url)
pars= BeautifulSoup(page,'html.parser')
price= pars.find('div',attrs={'class':'price-value'})

print('The price of BTC right now is '+price.text.strip())
