import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[['customer_number']].mode()
    return df