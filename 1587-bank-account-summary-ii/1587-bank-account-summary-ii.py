import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.groupby('account')['amount'].sum().reset_index(name = 'balance')
    print(transactions)
    df = transactions[transactions['balance'] > 10000].merge(users, on = 'account')
    return df[['name', 'balance']]