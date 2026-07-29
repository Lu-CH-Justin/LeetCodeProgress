import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values('product')
    df = activities.groupby('sell_date').agg(num_sold = ('product','size'),products = ('product', ','.join)).reset_index()
    return df