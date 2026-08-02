import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method = 'dense', ascending = False)
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id')
    df = df[df['rank'] == 1]
    return df[['name_y', 'name_x', 'salary']].rename(columns = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})