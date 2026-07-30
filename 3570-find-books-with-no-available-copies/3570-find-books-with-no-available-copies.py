import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    df = borrowing_records[borrowing_records['return_date'].isna()]
    df = df.groupby('book_id').size().reset_index(name = 'count')
    df2 = library_books.merge(df, on = 'book_id')
    df2 = df2[df2['total_copies'] - df2['count'] == 0]
    return df2[['book_id', 'title', 'author', 'genre', 'publication_year', 'total_copies']].rename(columns = {'total_copies': 'current_borrowers'}).sort_values(['current_borrowers', 'title'], ascending = [False, True])