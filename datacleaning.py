# %%
import numpy as np
import pandas as pd
import os

file_list = [file for file in os.listdir('./myoutput/')]
file_list

# %%
df_list = []
for file_name in file_list:
    df_list.append(pd.read_csv(f'./myoutput/{file_name}'))
df = pd.concat(df_list, ignore_index=True)
df

# %% [markdown]
#### Drop row that value is column name.

# %%
df = df[df['Order ID']!='Order ID']
df['Order ID']=='Order ID'

# %% [markdown]
#### Drop Nan value in df.

# %%
# df.dropna(how='any')
# df
print(df.isnull().values.any())
df.dropna(inplace=True)
df.isnull().values.any()

# %% [markdown]
#### Export to one file

# %%
df.to_csv('cleaned_data.csv', index=False)