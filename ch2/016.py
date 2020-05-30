import pandas as pd
import sys


if len(sys.argv) < 2:
    print('Set arg number of line.')
    sys.exit()
n = int(sys.argv[1])
df = pd.read_csv('./data/popular-names.txt', header=None, sep='\t')
df_nlist = [df.loc[i:i+n-1, :] for i in range(0, len(df), n)]
for dfi in df_nlist:
    print(dfi)
