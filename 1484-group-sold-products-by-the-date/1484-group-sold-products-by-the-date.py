import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values('product')
    df = activities.groupby('sell_date')['product'].agg(num_sold = 'size',products = ','.join).reset_index()
    return df