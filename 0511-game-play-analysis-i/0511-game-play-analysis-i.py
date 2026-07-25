import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id')['event_date'].min()
    return df.reset_index().rename(columns={'event_date': 'first_login'})