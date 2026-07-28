import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    queries['poor_query_percentage'] = (queries['rating'] < 3) * 100
    queries = queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().reset_index()
    queries['poor_query_percentage'] = queries['poor_query_percentage'].apply(lambda x: round(x + 1e-9, 2))
    queries['quality'] = queries['quality'].apply(lambda x: round(x + 1e-9, 2))
    return queries
