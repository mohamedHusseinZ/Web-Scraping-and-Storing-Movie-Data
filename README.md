# Web-Scraping-and-Storing-Movie-Data

Web Scraping and Storing Movie Data: README
Overview
This project fetches data from a web page containing a list of the 100 most highly-ranked films, extracts details about the top 50 films, and saves the information into a CSV file and an SQLite database. It leverages requests and BeautifulSoup for web scraping, pandas for data manipulation, and sqlite3 for database storage.

Features
Scrapes movie rankings from a web page.
Extracts movie rank, title, and release year.
Stores the extracted data in two formats:
A CSV file (top_50_films.csv).
An SQLite database (Movies.db).
Requirements
Python 3.x
Required packages:
requests
beautifulsoup4
pandas
sqlite3 (included with Python)
You can install the required libraries using pip:

bash
Copy code
pip install requests beautifulsoup4 pandas
How to Run
Clone or download the script.

Run the script.
The script will:

Fetch the movie data from the provided URL.
Extract the top 50 movies and save them to both a CSV file and an SQLite database.
Example command to run the script:

bash
Copy code
python script.py
Output.

A CSV file named top_50_films.csv will be created in the current directory.
An SQLite database named Movies.db will be created with a table called Top_50.
Files Generated
top_50_films.csv: A CSV file containing the top 50 films with columns: Average Rank, Film, and Year.
Movies.db: An SQLite database containing a table named Top_50 with the same columns.
License
This project is licensed under the MIT License.
