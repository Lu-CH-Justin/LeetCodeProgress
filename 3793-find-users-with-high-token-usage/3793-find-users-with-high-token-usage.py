import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    prompts['avg_tokens'] = prompts.groupby('user_id')['tokens'].transform('mean')
    valid = prompts[prompts['tokens'] > prompts['avg_tokens']]['user_id']
    df = prompts.groupby('user_id')['tokens'].agg(prompt_count = 'count', avg_tokens = 'mean').round(2).reset_index()
    df = df[(df['prompt_count'] >= 3) & (df['user_id'].isin(valid))]
    return df.sort_values(['avg_tokens', 'user_id'], ascending = [False, True])