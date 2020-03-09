import pandas as pd
import numpy as np

# # setting the number of rows for the CSV file
# N = 1000000
# # creating a pandas dataframe (df) with 8 columns and N rows with random integers between 999 and 999999 and with column names from A to H
# df = pd.DataFrame(np.random.randint(999,999999,size=(N, 7)), columns=list('ABCDEFG'))
# # creating one column 'H' of float type using the uniform distribution
# df['H'] = np.random.rand(N)
# # creating two additional columns with random strings
# df['I'] = pd.util.testing.rands_array(10, N)
# df['J'] = pd.util.testing.rands_array(10, N)
# # print the dataframe to see what we have created
# print(df)
# # export the dataframe to csv using comma delimiting
# df.to_csv("random.csv", sep=',',index=False)



import csv  
with open("random.csv") as csvfile:  
    data = csv.DictReader(csvfile)
    for row in data:
        print(row['A'])

data = csv.DictReader(open("random.csv"))
    for row in data:
        print(row['A'])