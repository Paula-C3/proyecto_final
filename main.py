!pip install pandas

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df_streaming = pd.read_json(/Users/paulacaicedo/Desktop/proyecto final/StreamingHistory0.json')
df_streaming.head()

# null values
pd. isnull (df_streams).sum()

df_streaming.info()

sorted_df=df_streaming.sort_values('popularity', ascending=true).head(10)sorted_df

df_streaming.describe().transpose 