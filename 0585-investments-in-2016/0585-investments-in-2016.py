import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['dupe'] = insurance.duplicated(['lat', 'lon'], keep = False)
    insurance['dupe2'] = insurance.duplicated('tiv_2015', keep = False)
    df = insurance[(insurance['dupe'] == False) & (insurance['dupe2'] == True)]
    return pd.DataFrame({'tiv_2016' : [df['tiv_2016'].sum().round(2)]})