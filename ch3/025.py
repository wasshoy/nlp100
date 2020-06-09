from collections import OrderedDict
import pandas as pd
import re

"""
Wikipediaの基礎情報のテンプレート表現
省略されている項目もある
{{基礎情報 国\n
|自治領等 = 
|略名 = イギリス\n
|日本語国名 = グレートブリテン及び北アイルランド連合王国\n

...

|国際電話番号 = 44\n
|注記 = <references />\n
}}\n
これから最終的に {フィールド名:値} を作る
"""

df = pd.read_json('./input/raw/jawiki-country.json', lines=True)
uk_data = df.query('title == "イギリス"')['text'].values
uk_text = uk_data[0]  # 今回は行ごとに分けない

# まずは基礎情報全体を抽出
# 上のテンプレート表現を真似てパターンを書く
# re.DOTALL: .の対象に改行も含める
# re.MULTILINE: 複数行に分かれる場合、2行目以降もそれぞれ検索する
# re.VEROBOSE: 空白、コメントをパターンから無視する
basic_info = re.search(r'''
                    ^
                    \{\{基礎情報.*?\n  # 基礎情報 国 の部分をキャプチャ (連続系特殊文字(今回は *) + ? で非貪欲マッチング（最小限の長さでマッチング）)
                    (.*?)                # |略名 ~ <refrerences/ >までをキャプチャ
                    \}\}
                    $
                     ''', uk_text, re.MULTILINE+re.VERBOSE+re.DOTALL)

print(basic_info.group(0))  # 探索した結果全体を表示(今回は1つだけ)

# フィールド名と値を抽出
# OrderDictを使って順序を保った辞書にする
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
print('-' * 50)
print(*[f'{key}: {value}' for key, value in templates.items()], sep='\n')
