import sys
from bs4 import BeautifulSoup
import pandas as pd
import requests

# url tested
# https://en.wikipedia.org/wiki/List_of_countries_by_financial_assets_per_capita

# Get the URL
print("Enter the URL of the Wikipedia page you want to scrape")
url = input()

# test if the URL is valid
try:
    response = requests.get(url)
except:
    sys.exit("Invalid URL")

    # test if the URL is from wikipedia
if "wikipedia" not in url:
    print("This is not a Wikipedia page")

# fetch the data
soup = BeautifulSoup(response.text)

# find the table
data = soup.find_all("table")[0]

# convert the table to a dataframe
df = pd.read_html(str(data))[0]

# print the shape of the dataframe
print("The shape of the dataframe is: ")
print(df.dtypes)
