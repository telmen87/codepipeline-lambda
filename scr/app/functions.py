import pandas as pd 
import numpy as np 


def get_df()->pd.DataFrame:
    df_dict = {
        "A" : [1, 2, 3],
        "B" : [4, 5, 6],
    }    
    return pd.DataFrame(df_dict)

