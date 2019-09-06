import pandas as pd
import numpy as np

df = pd.read_csv("all_mus_happy.csv",header=None)

df['positive_labels'] = df[[3,4,5,6,7,8]].apply(lambda x: ', '.join(x[x.notnull()]), axis = 1)
