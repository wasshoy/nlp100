with open('./data/popular-names.txt', 'r') as f:
    read_data = f.readlines()  # 一行ごとに分割したリストで取得
read_data = list(map(lambda line: line.replace('\t', ' '), read_data))
print(read_data[:3])
