import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person['email'].duplicated()]
    return df[['email']].drop_duplicates().rename(columns = {'email': 'Email'})