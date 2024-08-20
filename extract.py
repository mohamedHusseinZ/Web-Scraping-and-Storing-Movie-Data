import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

# Fetch the web page
url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the movie data
movies = []
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

for row in rows[1:51]:  # Extract top 50 films
    cells = row.find_all('td')
    if len(cells) >= 3:
        rank = cells[0].get_text(strip=True)
        film = cells[1].get_text(strip=True)
        year = cells[2].get_text(strip=True)
        movies.append({
            'Average Rank': rank,
            'Film': film,
            'Year': year
        })

# Convert to DataFrame
df = pd.DataFrame(movies)

# Save to CSV
csv_filename = 'top_50_films.csv'
df.to_csv(csv_filename, index=False)

# Save to SQLite database
db_filename = 'Movies.db'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS Top_50 (
    Average_Rank TEXT,
    Film TEXT,
    Year TEXT
)
''')

# Insert data
df.to_sql('Top_50', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()

print(f"Data has been successfully saved to {csv_filename} and {db_filename}.")
