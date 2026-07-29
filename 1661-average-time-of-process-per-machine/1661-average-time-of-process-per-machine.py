import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['machine_id', 'process_id','activity_type'], ascending = [True, True, False])
    activity['processing_time'] = activity.groupby(['machine_id', 'process_id'])['timestamp'].diff()
    return activity.groupby('machine_id')['processing_time'].mean().round(3).reset_index()