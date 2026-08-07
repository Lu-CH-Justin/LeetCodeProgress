import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders['order_date'].dt.year == 2019]
    df = users.merge(orders, left_on = 'user_id', right_on = 'buyer_id', how = 'left')
    print(df)
    df['orders_in_2019'] = df.groupby('user_id')['item_id'].transform('count')
    return df[['user_id', 'join_date', 'orders_in_2019']].drop_duplicates().rename(columns = {'user_id': 'buyer_id'})