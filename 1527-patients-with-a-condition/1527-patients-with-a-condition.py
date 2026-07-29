import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.contains(r'(^|\s)DIAB1')]
    return df