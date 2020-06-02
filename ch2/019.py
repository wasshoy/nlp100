from collections import Counter
import pandas as pd
df = pd.read_csv('./data/popular-names.txt', header=None, sep='\t')
# 解１：Counterを使う
# print(type(df[0]))  # Series
# print(type(df[[0]]))  # DataFrame
# counter = Counter(df[0])  # SeriesにはつかえるけどDataFrameには使えないから注意
# result_1 = [c for c in counter.keys()]
# print(*result_1, sep='\n')

# 解2: Seriesのuniqueメソッドを使う
result_2 = df[0].unique()  # デフォルトで頻度が高井淳
print(*result_2, sep='\n')
