import pandas as pd
df = pd.read_csv('./data/popular-names.txt', header=None, sep='\t')
# df.columns = ['name', 'sex', 'number', 'year']
df_sorted = df.sort_values(2, ascending=False)
print(df_sorted.head())
