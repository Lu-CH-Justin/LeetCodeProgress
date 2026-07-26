import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers['num'] = my_numbers['num'].drop_duplicates(keep = False)
    return my_numbers.sort_values('num', ascending = False).head(1)