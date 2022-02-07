import json
import urllib.request
import urllib.parse
from src.domain.currency import Currency

class CurrencyProxy():


    def get(self,url):
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        currencies = []  

        for currencyDict in dict:
            currency = Currency(id=currencyDict['id'], description=currencyDict['description'])
            currencies.append(currency)
        return currencies