import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    department = department.pivot(index = 'id', columns = 'month', values = 'revenue').reindex(columns = months).add_suffix('_Revenue')
    return department.reset_index()