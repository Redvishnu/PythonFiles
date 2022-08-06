import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests
url = "https://quotes.toscrape.com/"
response = requests.get(url)
response.status_code
soup = BeautifulSoup(response.content, 'html.parser')
quote = soup.findAll('span' , class_='text')
dataset = pd.DataFrame(quote)
print(dataset)
