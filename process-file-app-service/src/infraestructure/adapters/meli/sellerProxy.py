import json
import urllib.request
import urllib.parse
from src.domain.seller import Seller


class SellerProxy():

    def get(self, urlEndPoint):

        try:
            response = urllib.request.urlopen(urlEndPoint)
            data = response.read()
            dict = json.loads(data)
            if(response.code == 200):
                idSeller = None
                nameSeller = None
                try:
                    idSeller = dict["id"]
                except:
                    idSeller = None
                try:
                    nameSeller = dict["nickname"]
                except:
                    nameSeller = None
                seller = Seller(idSeller, nameSeller)
                return seller
            else:
                return None
        except:
            return None
