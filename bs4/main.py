from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

print(soup.prettify())


