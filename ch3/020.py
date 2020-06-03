import json
import pandas as pd


df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
# print(df.head())
print(df.query('title == "イギリス"')['text'].values[0])

# 21~29で使用するため保存
df.to_json('./input/processing/jawiki-irish-text.json')
