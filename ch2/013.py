import pandas as pd


df1 = pd.read_csv('./output/012py-output-col1.txt', names=['name'])
df2 = pd.read_csv('./output/012py-output-col2.txt', names=['sex'])

df_join = df1.join(df2)
df_join.to_csv('./output/013py-output.txt', sep='\t', index=None, header=None)
#

# 別解
"""
df = pd.concat([df1, df2], axis=1)
"""
