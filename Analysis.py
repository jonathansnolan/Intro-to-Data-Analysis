import pandas as pd

data2008 = pd.read_csv("08tstcar.csv")
print(data2008.head())
print(len(data2008.columns))
