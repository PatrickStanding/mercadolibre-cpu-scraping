import json
from logging import exception
import requests

class mercadolibreAPI:
    site="https://api.mercadolibre.com/sites/MLA/"
    categoryid=""
    options=[]


    def request_get(self,url):
        requests.get(url).json()
        try:
            return requests.get(url).json()
        except:
            return exception

    def test(self):
        #temporary function to test how classes+objetc+functions work maybe i shoul call it debug
        print(self.site)

    def get_category(self,subcategory=""):
        """
        #### returns a json with every category name and id
        
        ## Parameters:
        
        subcategory: string
            to get subcategory/child category use "parent-id"
            defualt = ""

        """
        url=self.site+"categories"
        if subcategory!="":
            url="https://api.mercadolibre.com/categories/"+subcategory
        print(f"getting url: {url}")
        response=self.request_get(url)
    
        "https://api.mercadolibre.com/sites/MLA/categories"
        return response

#quiero llegar a https://api.mercadolibre.com/sites/MLA/search?category=MLA1693&offset=50