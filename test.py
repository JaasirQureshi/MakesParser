import pandas as pd

df  = pd.read_csv('makes.csv')

for k,g in df.groupby('make'):
    print(k)
    for _,r in g.iterrows():
        print(f'  {r["model"]} ({r["yearStart"]-2000:02d}-{r["yearEnd"]-2000:02d})')


