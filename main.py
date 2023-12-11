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

sorted_df=df_streaming.sort_values('msPlayed', ascending=True).head(10)sorted_df

df_streaming.describe().transpose

most_popular=df_streaming.query('popularity>10000', inplace=False).sort_values('msPlayer', ascending=False)
most_popular[:10]

df_streaming.set_index("release_date", inplace=True)


#In[13]
sample_df=df_streaming.sample(int(0.004*len(df_streaming)))
#In[14]
print(len(sample_df))

#In[15]
plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y="msPlayer",x="artistName",color ="c").set(title="Loudness vs Energy Correlation")

#In[16]
#plt.figure(figuresize(10,6)
#sns.regplot(data=sample_df,y="msPlayer",x="acousticness", color="b").set(title="msPlayer vs Acousticness Correlation")

#In[21]
#df_gender=pd.read_csv("/Users/paulacaicedo/Desktop/proyecto final/MyData copy/YourLibrary.json")
#In[22]
#df_gender.head()















