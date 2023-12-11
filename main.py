!pip install pandas

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df_streaming = pd.read_json('StreamingHistory0.json')
df_streaming.head()
