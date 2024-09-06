# Importiamo la libreria pandas per la manipolazione dei dati
import pandas as pd

# Carichiamo il dataset
df = pd.read_csv("PATH/test.csv")
df.head(1)  # Visualizziamo la prima riga del dataframe per verificare il caricamento

# Elenco delle colonne da eliminare, che non sono utili per l'analisi
colonne_da_eliminare = [
    "returned_at", "shipped_at", "delivered_at", "inventory_item_id", "Unnamed: 0", "order_id_1", 
    "user_id_1", "status_1", "created_at_1", "shipped_at_1", "delivered_at_1", "returned_at_1", 
    "id_1", "department", "sku", "distribution_center_id", "id_2", "gender_1", "street_address", 
    "postal_code", "created_at_2"
]

# Rimuoviamo le colonne non necessarie
df = df.drop(columns=colonne_da_eliminare)
df.head(1)  # Visualizziamo la prima riga per verificare le modifiche

# Funzione per categorizzare i capi di abbigliamento in base alla stagione
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
    
    # Restituiamo la stagione appropriata in base alla categoria
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

# Esempio di utilizzo della funzione di categorizzazione
categorie = [
    'Accessories', 'Plus', 'Swim', 'Active', 'Socks & Hosiery', 'Socks', 'Dresses', 
    'Pants & Capris', 'Fashion Hoodies & Sweatshirts', 'Skirts', 'Blazers & Jackets', 
    'Suits', 'Tops & Tees', 'Sweaters', 'Shorts', 'Jeans', 'Maternity', 'Sleep & Lounge', 
    'Suits & Sport Coats', 'Pants', 'Intimates', 'Outerwear & Coats', 'Underwear', 
    'Leggings', 'Jumpsuits & Rompers', 'Clothing Sets'
]

# Testiamo la funzione con alcune categorie
for categoria in categorie:
    print(f"{categoria}: {categorizza_abbigliamento(categoria)}")

# Applichiamo la funzione di categorizzazione al dataframe per aggiungere la colonna "stagione"
df['stagione'] = df['category'].apply(categorizza_abbigliamento)
df.head(1)  # Verifichiamo l'aggiunta della colonna "stagione"

# Arrotondiamo i valori dei prezzi a due decimali
df["retail_price"] = df["retail_price"].round(2)
df["cost"] = df["cost"].round(2)
df["sale_price"] = df["sale_price"].round(2)
df.head(1)  # Verifichiamo le modifiche

# Esportiamo il dataframe in un file Excel
df.to_excel("PATH/CapstoneFinale.xlsx", index=False)
