import pandas as pd

pd.set_option('display.max_columns', None)


df = pd.read_csv("tomshardware.csv")
missing_data = df.isnull().sum()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(missing_data)
print(df.dtypes)

print(df.head())




