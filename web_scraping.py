import requests
from bs4 import BeautifulSoup
response = requests.get("https://brain-mentors.com/")

soup = BeautifulSoup(response.text , "html.parser")
# print(soup)
# print(response.text)

headings = soup.select("a")

for heading in headings:
    print(heading.get("href"))

