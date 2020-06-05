import json
import pandas as pd


# .jsonlファイルや一行のjsonはkines=Trueで読み込む必要がある
df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
# print(df.head())
print(df.query('title == "イギリス"')['text'].values)
# print(type(df.query('title == "イギリス"')['text'].values))
# for data in df.query('title == "イギリス"')['text'].values:
#     print(data)
