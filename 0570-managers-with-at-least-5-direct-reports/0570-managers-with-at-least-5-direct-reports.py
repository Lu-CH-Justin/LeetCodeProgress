import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name = 'count')
    df = df[df['count'] >= 5]
    df1 = df.merge(employee, left_on = 'managerId', right_on = 'id')
    return df1[['name']]