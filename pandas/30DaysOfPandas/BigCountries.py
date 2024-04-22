import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries_df = world[(world['area'] >= 3000000) | (world    ['population'] >= 25000000)] #? | Determines whether the area has 3000000 km^2 or more
    return big_countries_df[['name', 'population', 'area']] #? | Returns the "name", "population" & "area" columns

##################
# Status: SOLVED #
##################
