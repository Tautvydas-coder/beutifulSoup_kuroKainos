import requests
from bs4 import BeautifulSoup
from lxml import html
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}
page = requests.get(url='http://www.degalukainos.lt', headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='news').find('table', id="kainos").find_all('td')
# print(results)
body = soup.find('body').find('div').find('a').find_next('img')
print(body)

# print(soup)

root = html.fromstring(page.text)
tree = root.getroottree()
result = root.xpath('/html/body//*')


def write_to_file(result):
    with open('xpaths.csv', 'w') as file:
        for r in result:
            xpath = tree.getpath(r)
            file.write(xpath)
            file.write('\n')


write_to_file(result)
