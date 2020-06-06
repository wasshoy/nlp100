import pandas as pd
import re


def main():
    df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
    uk_data = df.query('title == "イギリス"')['text'].values
    # print(type(uk_df))
    uk_text_lines = uk_data[0].split('\n')  # ndarrayなので中身のstrを取り出し改行で区切る
    # 正規表現モジュールreを用いて"Category"を含む文字列を抽出
    pattern = re.compile('Category')
    categories = [line for line in uk_text_lines if re.search(pattern, line)]
    print(*categories, sep='\n')


# filterを使った別解
def ano_solution():
    df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
    uk_text = df.query('title == "イギリス"')['text'].values
    uk_text_lines = uk_text[0].split('\n')  # ndarrayなので中身のstrを取り出し改行で区切る
    categories = list(filter(lambda s: 'Category' in s, uk_text_lines))
    print(*categories, sep='\n')


ano_solution()
