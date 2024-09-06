# %%
import pandas as pd
df=pd.read_csv("C:\Program Files\Python312\python-homework\myspace\homework\CAPSTONE/test.csv")
df.head(1)

# %%
colonne_da_eliminare=["returned_at","shipped_at","delivered_at","inventory_item_id","Unnamed: 0","order_id_1","user_id_1","status_1","created_at_1","shipped_at_1", "delivered_at_1","returned_at_1","id_1", "department", "sku", "distribution_center_id", "id_2", "gender_1", "street_address", "postal_code", "created_at_2"] #eliminiamo le
df=df.drop(columns=colonne_da_eliminare)
df.head(1)

# %%
def categorizza_abbigliamento(categoria):
    estate = ['Swim', 'Shorts']
    inverno = ['Sweaters', 'Outerwear & Coats', 'Fashion Hoodies & Sweatshirts']
    primavera = ['Dresses', 'Skirts', 'Tops & Tees', 'Pants & Capris']
    autunno = ['Blazers & Jackets', 'Suits', 'Jeans', 'Leggings']
    tutto_l_anno = [
        'Accessories', 'Plus', 'Active', 'Socks & Hosiery', 'Socks', 
        'Maternity', 'Sleep & Lounge', 'Suits & Sport Coats', 'Pants', 
        'Intimates', 'Underwear', 'Jumpsuits & Rompers', 'Clothing Sets'
    ]
    
    if categoria in estate:
        return 'Summer'
    elif categoria in inverno:
        return 'Winter'
    elif categoria in primavera:
        return 'Spring'
    elif categoria in autunno:
        return 'Autumn'
    elif categoria in tutto_l_anno:
        return 'All Seasons'
    else:
        return 'Categoria non riconosciuta'

# Esempio di utilizzo
categorie = [
    'Accessories', 'Plus', 'Swim', 'Active', 'Socks & Hosiery', 'Socks', 'Dresses', 
    'Pants & Capris', 'Fashion Hoodies & Sweatshirts', 'Skirts', 'Blazers & Jackets', 
    'Suits', 'Tops & Tees', 'Sweaters', 'Shorts', 'Jeans', 'Maternity', 'Sleep & Lounge', 
    'Suits & Sport Coats', 'Pants', 'Intimates', 'Outerwear & Coats', 'Underwear', 
    'Leggings', 'Jumpsuits & Rompers', 'Clothing Sets'
]

for categoria in categorie:
    print(f"{categoria}: {categorizza_abbigliamento(categoria)}")

# %%
df['stagione'] = df['category'].apply(categorizza_abbigliamento)
df.head(1)

# %%
df["retail_price"]=df["retail_price"].round(2)
df["cost"]=df["cost"].round(2)
df["sale_price"]=df["sale_price"].round(2)
df.head(1)

# %%
df.to_excel("C:\Program Files\Python312\python-homework\myspace\homework\CAPSTONE/CapstoneFinale.xlsx", index=False)


