##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
df = pd.read_csv('tbl0.tsv',sep='\t', header=0)
dfg = df['_c0'].groupby([df['_c1']]).count()
print(dfg)
