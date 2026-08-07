import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products = products.sort_values(['product_id', 'change_date'])
    df = products[['product_id']].drop_duplicates().reset_index(drop = True)
    products = products[products['change_date'] <= '2019-08-16'].drop_duplicates('product_id', keep = 'last')
    df = df.merge(products, on = 'product_id', how = 'left')
    return df.fillna(10)[['product_id', 'new_price']].rename(columns = {'new_price': 'price'})