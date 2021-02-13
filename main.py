import requests
import selenium
from bs4 import BeautifulSoup

# website url to scrap from
url = ""
page = requests.get(url)
parsed = BeautifulSoup(page.content, "html.parser")

# Specify element by id
results = parsed.find(id="")

print(results.prettify())

# Iterate through elements under same classname
elems = results.find_all('section', class_='')

for elem in elems:
    print(elem, end='/n')