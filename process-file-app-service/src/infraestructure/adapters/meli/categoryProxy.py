from datetime import datetime
import json
from unicodedata import category
import urllib.request
import urllib.parse
from src.domain.category import Category


class CategoryProxy():

    def get(self, urlEndPoint):
        categories = []
        try:
            response = urllib.request.urlopen(urlEndPoint)
            data = response.read()
            dict = json.loads(data)
            if(response.code == 200):
                for catDic in dict:
                    idCategory = None
                    nameCategory = None
                    try:
                        idCategory = catDic["id"]
                    except:
                        idCategory = None
                    try:
                        nameCategory = catDic["name"]
                    except:
                        nameCategory = None   
                    category = Category(idCategory,nameCategory)
                    categories.append(category)
                return categories  
            else:
                return categories
        except:
            return categories
