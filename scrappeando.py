import json
from logging import exception
from unittest import result
import requests

class mercadolibreAPI:

    site="https://api.mercadolibre.com/sites/MLA/"
    categoryid=None
    item=None
    debugmode=False
    limit=50
    debuglimit=5
    def set_debug(self, debug=True):
        """
        Enables debugmode.
        - sets querry results limit to 5 (default=50)
        
        ## Parameters

        debug: boolean
           Default=False
        
        """
        self.debugmode = debug
        if(self.debugmode)==True: print("Modo Debug ENCENDIDO")
        print(debug)

    def request_get(self,url):
        """
        Get json from given url.
        url: str
        """
        if self.debugmode:
            url+= "&limit=" + str(self.debuglimit)
        else:
            url+="&limit="+ str(self.limit)
        print(url)
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
        returns a json with every category name and id
        
        ## Parameters:
        
        subcategory: string
            to get subcategory/child category use "parent-id"
            defualt = NULL
        """

        url=self.site+"categories"
        if subcategory!="":
            url="https://api.mercadolibre.com/categories/"+subcategory
        #TODO: complete sucategory

        print(f"getting url: {url}")
        response=self.request_get(url)
    
        "https://api.mercadolibre.com/sites/MLA/categories"
        return response

    def item_search(self,item,categoryid=None):
        """
        Returns json response of search result for given item.
        If category id isn't specified on class definition then the item is searched on every category.


        ## Parameters:
        item: str
            product to search
        categoryid: str
            optional variable to search item on specified categoryid and set is as self.categoryid
            default= mercadolibreAPI.category
        """
        
        item=item.replace(" ","%")
        item

        self.item=item
        
        if categoryid==None:
            
            #serchs item on every category
            url=self.site + "search?" + "q=" + item
            print(f"searchin {item}\t{url=}")
            result=self.request_get(url)
        
        else:
            #search item on specified category
            self.categoryid=categoryid
            url=self.site + "search?" + "q=" + item + "&category=" +self.categoryid
            print(f"searchin {item}\t{url=}")
            result=self.request_get(url)
        
        return result

#quiero llegar a https://api.mercadolibre.com/sites/MLA/search?category=MLA1693&offset=50