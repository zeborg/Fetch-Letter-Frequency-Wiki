import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Letter_frequency').content
soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

tr = tables[0].select('tr')

print(40*'-')
print('L: Language\t\tD: Dictionary')
print(40*'-')
print('Letter\tFrequency (L)\tFrequency (D)')
print(40*'-')
for i in tr:
  j = i.select('td')
  if len(j) != 0:
    print(j[0].text+'\t'+j[1].text.rstrip()+'\t\t'+j[3].text)
