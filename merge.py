"""
import pandas as pd

scraped = pd.read_csv('scraped_data.csv')
df = pd.read_csv('dwarf_stars.csv')
df.dropna()

df['Mass'] = df['Mass'].astype(float)
df['Radius'] = df['Radius'].astype(float)
df['Mass'] = df['Mass'] * 0.000954588
df['Radius'] = df['Radius'] * 0.102763

merge_stars_df = pd.merge(df,scraped)
merge_stars_df.to_csv('merged_stars.csv')
"""