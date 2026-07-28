import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on = 'product_id', how = 'left')
    print(df)
    df = df[df['purchase_date'].between(df['start_date'], df['end_date'])]
    df['total'] = df['price'] * df['units']
    df = df.groupby('product_id')[['units', 'total']].sum().reset_index()
    df['average_price'] = df['total'] / df['units']
    df = prices[['product_id']].drop_duplicates().merge(df[['product_id', 'average_price']], on = 'product_id', how = 'left')
    df['average_price'] = df['average_price'].fillna(0)
    return df.round(2)