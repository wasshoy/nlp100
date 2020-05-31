import pandas as pd
df = pd.read_csv('./data/popular-names.txt', header=None, sep='\t')
# 一列目のユニークな値を取得
col1_uniq = df[0].unique()
print(col1_uniq)
