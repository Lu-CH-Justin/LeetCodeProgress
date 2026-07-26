import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_df = orders.merge(company, on = 'com_id', how = 'left')
    filter_df = order_df[order_df['name'] == 'RED']
    df = sales_person[~sales_person['sales_id'].isin(filter_df['sales_id'])]
    return df[['name']]