import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['count'] = employee.groupby('employee_id')['department_id'].transform('count')
    print(employee)
    employee = employee[(employee['count'] == 1) | ((employee['count'] > 1) & (employee['primary_flag'] == 'Y'))]
    return employee[['employee_id', 'department_id']]