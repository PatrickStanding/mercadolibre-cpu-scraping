#%%
import scrappeando
import pandas as pd

ml=scrappeando.mercadolibreAPI()
    #Set the api

ml.limit=3 #number of results

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

df["Precio"]=df["Precio"].round(2)
df['Precio'] = df['Precio'].apply('{:,}'.format)

print(df[["Titulo","Precio"]])
