import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
import locale
import joblib

def file_import(filepath_in,filepath_out):

    df = pd.read_csv(filepath_in)

    # Strip leading and trailing whitespace from all column names
    df.columns = df.columns.str.strip()

    df.to_pickle(filepath_out)
    
    return df

    

if __name__ == '__main__':
    df = file_import('data/Chicago_Population_Counts.csv', 'data/pickled_df_chi_pop.pkl' )
    print("Dataframe with whitespace-stripped column names:")
    print(df.head(2))
