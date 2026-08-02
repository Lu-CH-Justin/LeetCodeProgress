import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.sort_values('salary', ascending = False).drop_duplicates('salary')
    if len(df) < N or N <= 0:
        ans = None
    else:
        ans = df.iloc[N-1, 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [ans]})