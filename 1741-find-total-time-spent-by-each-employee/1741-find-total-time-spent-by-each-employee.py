import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.groupby(['emp_id', 'event_day']).agg(in_time = ('in_time', 'sum'), out_time = ('out_time', 'sum')).reset_index()
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees[['event_day', 'emp_id', 'total_time']].rename(columns = {'event_day': 'day'})