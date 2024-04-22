import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')] #? | Finds all the results of both low fat and recyclable products and saves them to the 'result' variable
    return result[['product_id']]

##################
# Status: SOLVED #
##################
