from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(URL)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)
print(total_table)

temporary = []


table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temporary.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temporary)

for i in range(1,len(temporary)):
    
    Star_names.append(temporary[i][0])
    Distance.append(temporary[i][5])
    Mass.append(temporary[i][7])
    Radius.append(temporary[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")

scraped = pd.read_csv('scraped_data.csv')

df = pd.read_csv('dwarf_stars.csv')

df = df.dropna()

df = df[df['Mass'].str.isnumeric()]

df['Mass'] = df['Mass'].astype(float)
df['Radius'] = df['Radius'].astype(float)

df['Mass'] = df['Mass'] * 0.000954588
df['Radius'] = df['Radius'] * 0.102763

merge_stars_df = pd.merge(df, scraped, on=['id','Star_name', 'Distance', 'Mass', 'Radius'])

merge_stars_df.to_csv('merged_stars.csv', index=False)