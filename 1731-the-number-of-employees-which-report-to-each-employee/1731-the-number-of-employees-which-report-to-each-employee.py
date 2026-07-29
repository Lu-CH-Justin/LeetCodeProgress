import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df2 = employees.groupby('reports_to')['age'].agg(reports_count = 'count', average_age = 'mean').apply(lambda x: round(x + 0.0001,0)).reset_index()
    df = df2.merge(employees, left_on = 'reports_to', right_on = 'employee_id')
    return df[['employee_id', 'name', 'reports_count', 'average_age']]