from collections import OrderedDict
import pandas as pd
import re


# https://qiita.com/segavvy/items/f6d0f3d6eee5acc33c58

"""
Wikipediaのマークアップ早見表より
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
斜体：''文''
強調：'''文字'''
斜体と強調：''''''文字''''''
"""


df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
uk_data = df.query('title == "イギリス"')['text'].values
uk_text = uk_data[0]

# 基本情報テンプレートを抽出
basic_info = re.search(r'''
                    ^
                    \{\{基礎情報.*?\n  # 基礎情報 国 の部分をキャプチャ (連続系特殊文字(今回は *) + ? で非貪欲マッチング（最小限の長さでマッチング）)
                    (.*?)                # |略名 ~ <refrerences/ >までをキャプチャ
                    \}\}
                    $
                     ''', uk_text, re.MULTILINE+re.VERBOSE+re.DOTALL)

# フィールド名と値を抽出
# (フィールド名, 値)のタプルのリストが手に入るので順序を保った辞書化する
templates = OrderedDict(re.findall(r'''
                            ^
                            \|
                            (.+?)       # フィールド名
                            \s*         # フィールド名の次の空白
                            =
                            \s*
                            (.+?)       # フィールド名に対応する値
                            (?:         # 検索対象にはするが結果では除外する
                              (?=\n\|)  # 改行 + |(値と次のフィールド名の境目) を先読みアサーション(?=以降があとに続く場合マッチ)
                              |         # または
                              (?=\n$)   # 末尾の改行
                            )
                             ''', basic_info.group(1), re.MULTILINE+re.VERBOSE+re.DOTALL))

# 強調表現を表すパターン
patt_emp = re.compile(r"'{2, 5}.+'{2, 5}")
# 強調表現の除去した辞書にする
d = {k: re.sub(patt_emp, '', v) for k, v in templates.items()}
print(d)
