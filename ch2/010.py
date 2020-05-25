'''ファイルのパスが相対パスなので実行時このファイルがあるディレクトリで行う必要がある
'''
import pandas as pd


with open('./data/popular-names.txt', 'r') as f:
    read_data = f.readlines()  # 一行ごとに分割したリストで取得
print(f'行数: {len(read_data)}')

# 別解
df = pd.read_csv('./data/popular-names.txt', sep='\t', header=None)
print(f'行数: {len(df)}')
