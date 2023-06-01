import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://aldencutler.github.io/personal-website').text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify()) # You can use find() or find_all() (both are features of BeautifulSoup) to filter down which elements you want
# For example, if I wanted all the paragraph elements, I could do:
# p = soup.find_all('p')
