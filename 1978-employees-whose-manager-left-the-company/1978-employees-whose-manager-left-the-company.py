import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[(employees['salary'] < 30000) & (~employees['manager_id'].isin(employees['employee_id']))].dropna()[['employee_id']].sort_values('employee_id')