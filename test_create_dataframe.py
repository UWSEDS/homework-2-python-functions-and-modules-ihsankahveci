BabyNames = ('https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD')

import pandas as pd
df = pd.read_csv(BabyNames)

def test_create_dataframe (data_frame, column_names):
 
    if set(data_frame.columns) != set(column_names): 
        raise KeyError ("Column names are not found")
    
    if len(df.index) < 10:
        raise ValueError ("There are not enough rows.")
    
    if len(set(df.dtypes)) != 1:
        raise TypeError ("The values should be the same data type")
  
    return True 


colnames = df.columns
test_create_dataframe(df, colnames)
