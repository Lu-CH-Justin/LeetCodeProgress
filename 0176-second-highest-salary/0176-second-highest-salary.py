import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.sort_values('salary', ascending = False).drop_duplicates('salary')
    if len(df) > 1:
        return df.iloc[[1]][['salary']].rename(columns = {'salary': 'SecondHighestSalary'})
    return pd.DataFrame({'SecondHighestSalary': [None]})