import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree['type'] = None
    tree['type'] = tree['type'].case_when([(tree['p_id'] == None, 'Root'), (tree['p_id'].isin(tree['id']) & tree['id'].isin(tree['p_id']), 'Inner'), (tree['p_id'].isin(tree['id']) & ~tree['id'].isin(tree['p_id']), 'Leaf')])
    return tree[['id', 'type']]