import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first_login'] = activity.groupby('player_id')['event_date'].transform('min')
    activity.drop_duplicates(subset = ['player_id'], inplace = True)
    return activity[['player_id', 'first_login']]