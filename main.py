import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import csv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}
page = requests.get(url='http://www.degalukainos.lt', headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='news').find('table', id="kainos").find_all('td')
# print(results)

body = soup.find('body').find('div').find('h1')
for link in body:
    print(link.get_text())

# print(soup)

root = html.fromstring(page.content)
elements = root.xpath('//html/body/div/div[2]/div[1]/div[4]/div[1]/h2')
print(elements[0].text)

tree = root.getroottree()
result = root.xpath('/html/body/div//*')

dom = etree.HTML(str(root))


def write_to_file(result, dom):
    with open('xpaths.csv', 'w') as file:
        for r in result:
            xpath = tree.getpath(r)
            full_xpath = '/' + xpath
            file.write(full_xpath + '\n')
            print(r.get('r'))

if __name__ == '__main__':
    write_to_file(result, dom)
