from dataclasses import dataclass


@dataclass
class ItemResumen:

    itemEndPoint = None
    itemSite = None
    itemId = None
    itemPrice = None
    itemStartTime = None
    categoryID = None
    categoryName = None
    currencyID = None
    currencyDescription = None
    sellerID = None
    sellerNickName = None

    def __init__(self, itemSite, itemId):
        self.itemSite = itemSite
        self.itemId = itemId

    def getItemKey(self):
        return self.itemSite + self.itemId

    def setItemEndPoint(self, endpoint):
        self.itemEndPoint = endpoint+self.getItemKey()

    def __str__(self):

        return self.itemSite+"|"+self.itemId+"|"+self.getItemKey()
