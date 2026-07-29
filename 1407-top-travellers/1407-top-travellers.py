import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    rides = rides.groupby('user_id')['distance'].sum().reset_index()
    df = users.merge(rides, left_on = 'id', right_on = 'user_id', how = 'left')
    return df.sort_values(['distance', 'name'], ascending = [False, True]).fillna(0)[['name', 'distance']].rename(columns = {'distance': 'travelled_distance'})