import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on = 'product_id')
    invalid = df[~df['sale_date'].between('2019-01-01', '2019-03-31')]['product_id']
    df = df[(df['sale_date'].between('2019-01-01', '2019-03-31')) & ~(df['product_id'].isin(invalid))]
    return df[['product_id', 'product_name']].drop_duplicates()