import pandas as pd
import re


df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
uk_data = df.query('title == "イギリス"')['text'].values
uk_text_lines = uk_data[0].split('\n')
# print(uk_text_lines)
# 先頭が1個以上の=で始まり、任意の１文字が0回以上繰り返された後、末尾が1個以上の=で終わる文字列
pattern = re.compile('^=+.*=+$')
sec_names = [(line.replace('=', ''), line.count('=') // 2 - 1)
             for line in uk_text_lines if re.search(pattern, line)]
print(*sec_names, sep='\n')
