import os
import pandas as pd
# my_absolute_dirpath = os.path.abspath(os.path.dirname())
# print(my_absolute_dirpath)
df = pd.read_csv('/home/mohan/other_classes.csv',header=None)
df.info()
print(df.describe())
# print(tabulate(print_table, headers=headers))
print(df.columns)
df.dropna(axis=0, how='any')
df.replace(to_replace=None, value=None)
pd.isnull(object)
df.drop(1, axis=1)
print(df.values)
pd.to_numeric(df[1], errors='coerce')
df.loc[1]

#Operating on Dataframes
df["height"].apply(lambda height: 2 * height)
df.rename(columns = {df.columns[2]:'size'}, inplace=True)
df[0].unique()

#Accessing sub-data frames

new_df = df[[1,2]]

