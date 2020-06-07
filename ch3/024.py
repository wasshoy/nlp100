from typing import Pattern
import pandas as pd
import re


df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
uk_data = df.query('title == "イギリス"')['text'].values
uk_text_lines = uk_data[0].split('\n')
pattern = re.compile(r'\[\[(File|ファイル):(.+?)\|')

print(*[line
        for line in uk_text_lines if re.findall(pattern, line)], sep='\n')
