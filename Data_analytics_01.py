# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)

# %% 
df = pd.read_csv('dados_enem_2021_BA.csv')

df
# %%

df.head()
# %%
df.shape
# %%
df.info()
# %%
df.columns

# %%
## Verificar dados ausentes
(df.isna().sum() / df.shape[0] * 100).sort_values(ascending=False)

# %%
df.describe().transpose()
# %%

df.nunique().sort_values(ascending= True)

# %%
## Seleciona as colunas
df[['TP_ESCOLA', 'TP_SEXO']]
df.TP_ESCOLA# %%

# %%
## Seleciono da 1 linha até a 5 da columa 0
df.iloc[0:5, 0]
df.iloc[0:5, 1]

# %%

#df.select_dtypes(include= [int, float])
df.select_dtypes(include= [object])

# %%
df.select_dtypes(include= [ float, int]).columns.tolist()
# %%
