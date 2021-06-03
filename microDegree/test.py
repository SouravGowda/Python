import pandas as pd

df = pd.read_csv('product_to_track.csv')
df1 = pd.DataFrame(df)
print(df1['URL'])