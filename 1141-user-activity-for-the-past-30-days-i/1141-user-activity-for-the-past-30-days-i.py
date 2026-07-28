import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    start_date = pd.to_datetime('2019-07-27') - pd.Timedelta(days=29)
    df = activity[activity['activity_date'].between(start_date, '2019-07-27')]
    df = df.groupby('activity_date')['user_id'].nunique().reset_index()
    return df.rename(columns = {'activity_date': 'day', 'user_id': 'active_users'})