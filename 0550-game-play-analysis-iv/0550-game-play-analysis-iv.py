import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id','event_date'])
    activity['first'] = activity.groupby('player_id')['event_date'].transform('min')
    df = activity[(activity['event_date'] - activity['first']).dt.days == 1]
    return pd.DataFrame({'fraction': [round(df['player_id'].nunique() / activity['player_id'].nunique(), 2)]})