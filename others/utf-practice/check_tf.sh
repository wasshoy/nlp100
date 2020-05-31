# ファイルの内容を確認
cat kana.txt
# ファイルの変換方式(translate format)の確認
file --mime kana.txt
# 16進数、1バイト区切りで変換して表示
od -t x1 kana.txt
# エンディアンの種類はBOM(Byte Order Mark)があればその方向で確認できるが、ファイルによってBOMがあったりなかったりする
# エンディアンはCPUの種類によって依る
# BOMの確認はfileコマンドでできる(BOMがある場合(with BOM)と表示される)
# BOMがある場合は先頭2バイトに表示され、 fffe ならリトルエンディアン、feff ならビッグエンディアン