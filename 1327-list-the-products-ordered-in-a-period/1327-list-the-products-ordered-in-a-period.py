import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'].dt.year == 2020) & (orders['order_date'].dt.month == 2)]
    df = orders.groupby('product_id')['unit'].sum().reset_index()
    df = df[df['unit'] >= 100]
    df = df.merge(products, on = 'product_id')
    return df[['product_name', 'unit']]