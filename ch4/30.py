import pickle


import MeCab

# 公式 https://taku910.github.io/mecab/#parse より
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
# で出力される

# neko.txt.mecab を読み込み、各単語を辞書型で管理
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
with open('./input/neko.txt.mecab') as f:
    wakachi_words = f.read().split('\n')
res = []
for line in wakachi_words:
    # print(f'{line=}, {type(line)=}')
    if line == 'EOS' or line == ' ' or line == '':
        continue
    surface, rest, = line.split('\t')
    rest = rest.split(',')
    d = {}
    d['surface'] = surface
    d['base'] = rest[6]
    d['pos'] = rest[0]
    d['pos1'] = rest[1]
    res.append(d)
# python のオブジェクトとして保存
with open('./input/keitaiso_dict.pickle', 'wb') as wf:
    pickle.dump(res, wf)
