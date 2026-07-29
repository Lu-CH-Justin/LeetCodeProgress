import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('employee_id')['department_id'].count().reset_index()
    df = df[df['department_id'] == 1]['employee_id']
    employee = employee[(employee['employee_id'].isin(df)) | ((~employee['employee_id'].isin(df)) & (employee['primary_flag'] == 'Y'))]
    return employee[['employee_id', 'department_id']]