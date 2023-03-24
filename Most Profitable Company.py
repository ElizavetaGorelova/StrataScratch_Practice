import pandas as pd

df = forbes_global_2010_2014
df = df[df['profits']==df['profits'].max()]
df[['company', 'continent']]
