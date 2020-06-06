from re import search
import pandas as pd
import re


def main():
    df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
    uk_data = df.query('title == "イギリス"')['text'].values
    uk_text_lines = uk_data[0].split('\n')
    # 正規表現モジュールreを用いて"Category"を含む文字列を抽出
    pattern_1 = re.compile('Category:')
    pattern_2 = re.compile(r'\[\[')
    pattern_3 = re.compile(r'\]\]')
    pattern_4 = re.compile(r'\|\*')
    pattern_5 = re.compile(r'\|元')
    categories = [line for line in uk_text_lines if re.search(pattern_1, line)]
    print(*categories, sep='\n')
    categories_2 = [re.sub(pattern_5, '', re.sub(pattern_4, '', re.sub(pattern_3, '', re.sub(pattern_2, '', re.sub(pattern_1, '', line)))))
                    for line in categories]
    print(*categories_2, sep='\n')


main()
