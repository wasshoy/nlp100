import pandas as pd


with open('./data/popular-names.txt', 'r') as rf:
    lines = rf.readlines()
lines = list(map(lambda s: s.replace('\n', '').split('\t'), lines))
col_1 = ''.join([line[0] + '\n' for line in lines])
col_2 = ''.join([line[1] + '\n' for line in lines])

with open('./output/012py-output-col1.txt', 'w') as wf:
    wf.write(col_1)
with open('./output/012py-output-col2.txt', 'w') as wf:
    wf.write(col_2)

# 別解
df = pd.read_csv('./data/popular-names.txt', sep='\t', header=None)
df[0].to_csv('./output/012py-other-output-col1.txt', index=False, header=None)
df[1].to_csv('./output/012py-other-output-col2.txt', index=False, header=None)
