import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = request_accepted
    df1 = pd.concat([df['requester_id'], df['accepter_id']], ignore_index = True).reset_index(name = 'id')
    df2 = df1['id'].value_counts().reset_index(name = 'num')
    return df2.loc[[df2['num'].idxmax()]]