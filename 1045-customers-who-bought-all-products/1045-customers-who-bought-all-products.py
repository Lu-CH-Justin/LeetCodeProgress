import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer['unique'] = customer.groupby('customer_id').transform('nunique')
    return customer[customer['unique'] == len(product)][['customer_id']].drop_duplicates()