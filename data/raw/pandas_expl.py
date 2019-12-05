""" import os
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

# Sum of values in a data frame
df.sum()
# Lowest value of a data frame
df.min()
# Highest value
df.max()
# Index of the lowest value
df.idxmin()
# Index of the highest value
df.idxmax()
# Statistical summary of the data frame, with quartiles, median, etc.
df.describe()
# Average values
df.mean()
# Median values
df.median()
# Correlation between columns
df.corr()
# To get these values for only one column, just select it like this#
df["size"].median()

# Sorting the data

df.sort_values(ascending=False)

#Boolean indexing

df[df["size"]==5]

#Selecting values

# selcting specific row in the particular column

df.loc(['row_number'],['column_name']) """

""" Avoiding looping in our code while using python """
#Finding the sum of the squares in a list

x = [1,3,5,7,9]
sum_squared = 0

for i in range(len(x)):
    sum_squared+=x[i]**2

print(sum_squared)

for y in x:
    sum_squared+=y**2

print(">>>>>>",sum_squared)

sum_squared = sum(y**2 for y in x)
# This approach is called List Comprehension.
print(sum_squared)

#Using if else

x = [1,2,3,4,5,6,7,8,9]
even_squared = [y**2 for y in x if y%2==0]
print(even_squared)
# if we want to have the number squared for even and cubed for odd
squared_cubed =  [y**2 if y%2 ==0 else y**3 for y in x]

""" Using enumerate function """

L = ['blue','yellow', 'orange']
for i, val in enumerate(L):
    print("index is %d and value is %s" %(i,val))

############### Dictionary Comprehension ############

""" we're trying to get a dictionary with (key :squared value) for every value in x """

x = [1,2,3,4,5,6,7,8,9]

print({k: k**2 for k in x})

"""  dict only even values """
x = [1,2,3,4,5,6,7,8,9]

print({k:k**2 for k in x if k%2==0})

""" we're trying to find the squared value for even and cubed number for odd key """

x = [1,2,3,4,5,6,7,8,9]

print({k: k**2 if k%2==0 else k**3 for k in x})
