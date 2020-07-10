import MeCab
import subprocess

cmd = 'echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'  # NEologed の場所を出力するコマンド
path = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         shell=True).communicate()[0]).decode('utf-8')
tagger = MeCab.Tagger(f'-d {path}')
with open('./input/neko.txt') as f:
    text = f.read()
wakachi_text = tagger.parse(text)

with open('./input/neko.txt.mecab', 'w') as f:
    f.write(wakachi_text)
