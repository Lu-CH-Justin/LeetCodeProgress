import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[(~employees['employee_id'] % 2 == 0) & (~employees['name'].str.contains(r'^M'))]
    df = df.merge(employees, on = 'employee_id', how = 'right')
    return df[['employee_id', 'salary_x']].rename(columns = {'salary_x': 'bonus'}).fillna(0).sort_values('employee_id')