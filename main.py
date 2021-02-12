import requests
import selenium
from bs4 import BeautifulSoup

# website url to scrap from
url = ""
page = requests.get(url)
parsed = BeautifulSoup(page.content, "html.parser")

#Specify element by id
results = parsed.find(id="")

print(results.prettify())