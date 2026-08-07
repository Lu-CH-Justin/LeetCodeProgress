import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    df = transactions.groupby(['month','country'], dropna= False).agg(trans_count = ('id', 'count'), approved_count = ('state', lambda x: (x == 'approved').sum()),trans_total_amount = ('amount', 'sum'), approved_total_amount = ('amount', lambda x: x[transactions.loc[x.index, 'state'] == 'approved'].sum())).reset_index()
    return df

    # A faster and better way
    # first create the columns for approved
    #transactions['approved'] = transactions['state'] == 'approved'
    #transactions['approved_amount'] = 0
    #transactions.loc[transactions['approved'], 'approved_amount'] = transactions['amount']
    # then do groupby aggregation without lambda
    #df = transactions.groupby(['month', 'country'], dropna=False).agg(trans_count=('id', 'count'),approved_count=('approved', 'sum'),trans_total_amount=('amount', 'sum'),approved_total_amount=('approved_amount', 'sum')).reset_index()