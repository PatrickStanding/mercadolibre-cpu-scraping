#%%
import scrappeando
import requests
import json
import pandas as pd
import importlib as imp#only for debuging

ml=scrappeando.mercadolibreAPI()

def reset():
    imp.reload(scrappeando)
    global ml
    ml=scrappeando.mercadolibreAPI()

ml.set_debug()
#%%
test=ml.test()
categorias=ml.get_category()
#%%

categorias = pd.DataFrame(categorias)
print(categorias)


# url="https://api.mercadolibre.com/sites/MLA/categories"
# response=requests.get(url)
# print(response)
# print(response.json())

# %%

## searching item

search_cpus=ml.item_search("amd","MLA1693")

cpus=search_cpus["results"]



cpus_dataframe_data=[]

for item in cpus:
    title=item["title"]
    price=item["price"]
    condition=item["condition"]
    link=item["permalink"]
    item_dict={
        "Titulo":title,
        "Precio":price,
        "Condicion":condition,
        "Link":link
    }
    cpus_dataframe_data.append(item_dict)

df=pd.DataFrame(cpus_dataframe_data)

print(df)
# %%
