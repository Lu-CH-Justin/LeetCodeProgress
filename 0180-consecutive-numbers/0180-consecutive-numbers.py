import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev'] = logs['num'].shift(1)
    logs['next'] = logs['num'].shift(-1)
    df = logs[(logs['num'] == logs['prev']) & (logs['prev'] == logs['next'])]
    return df[['num']].drop_duplicates().rename(columns = {'num': 'ConsecutiveNums'})
