import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[products['description'].str.contains('( |^)SN[0-9]{4}-[0-9]{4}( |$)')].sort_values('product_id')