import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby('contest_id').size().reset_index(name = 'percentage')
    df['percentage'] = (df['percentage'] / users['user_id'].count() * 100).round(2)
    return df.sort_values(['percentage', 'contest_id'], ascending = [False, True])