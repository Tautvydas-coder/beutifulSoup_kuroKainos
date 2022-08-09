import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}
page = requests.get(url='http://www.degalukainos.lt', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find(class_='news').find('table', id="kainos").find_all('td')
print(results)

# print(soup)
