import urllib.request
from bs4 import BeautifulSoup
import urllib.error

url= 'https://cointelegraph.com/bitcoin-price-index'
page= urllib.request.urlopen(url)
pars= BeautifulSoup(page,'html.parser')
price= pars.find('span',attrs={'class':'price-value'}) #the html tag was div before, but now it's span

print('The price of BTC right now is '+price.text.strip())
