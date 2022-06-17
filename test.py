#%%
import scrappeando
import requests
import json
import pandas as pd
#%%
ml=scrappeando.mercadolibreAPI()
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
