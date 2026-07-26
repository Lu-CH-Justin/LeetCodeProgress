import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_df = orders.merge(company, on = 'com_id', how = 'left')
    filter_df = order_df[order_df['name'] == 'RED']
    df = sales_person.merge(filter_df, on = 'sales_id', how = 'left')
    df = df[df['com_id'].isna()]
    return df[['name_x']].rename(columns = {'name_x': 'name'})