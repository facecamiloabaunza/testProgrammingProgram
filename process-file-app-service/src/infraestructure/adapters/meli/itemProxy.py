from datetime import datetime
import json
import urllib.request
import urllib.parse
from src.domain.currency import Currency
from src.domain.itemResume import ItemResumen


class ItemProxy():

    def get(self, item):

        try:
            response = urllib.request.urlopen(item.itemEndPoint)
            data = response.read()
            dict = json.loads(data)
            if(response.code == 200):
                try:
                    item.itemPrice = dict["price"]
                except:
                    item.itemPrice = None
                try:
                    item.itemStartTime = dict["start_time"]
                except:
                    item.itemStartTime = None
                try:
                    item.categoryID = dict["category_id"]
                except:
                    item.categoryID = None
                try:
                    item.currencyID = dict["currency_id"]
                except:
                    item.currencyID = None
                try:
                    item.sellerID = dict["seller_id"]
                except:
                    item.sellerID = None
                return item
            else:
                return item
        except:
            return item
