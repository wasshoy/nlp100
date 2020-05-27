import sys
import pandas as pd

if len(sys.argv) < 2:
    print('Set arg number of line.')
    sys.exit()
n = int(sys.argv[1])
df = pd.read_csv('./data/popular-names.txt', header=None, sep='\t')
print(df.head(n))
