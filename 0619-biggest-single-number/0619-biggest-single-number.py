import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers['num'].value_counts().reset_index()
    df = df[df['count'] == 1]
    return pd.DataFrame({'num': [df['num'].max()]})