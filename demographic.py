import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')
df.sort_values("total_events", ascending=True)

output = df.head(20)