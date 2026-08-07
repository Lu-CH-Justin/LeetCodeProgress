import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values(['customer_id', 'order_date']).drop_duplicates('customer_id')
    delivery['immediate'] = delivery['order_date'] == delivery['customer_pref_delivery_date']
    return pd.DataFrame({'immediate_percentage': [round(delivery['immediate'].sum() / len(delivery) * 100, 2)]})