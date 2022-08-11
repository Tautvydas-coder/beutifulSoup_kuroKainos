import requests
from bs4 import BeautifulSoup
from lxml import html, etree
from itertools import zip_longest
import csv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}
page = requests.get(url='http://www.degalukainos.lt', headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='news').find('table', id="kainos").find_all('td')
# print(results)

body = soup.find('body').find('div').find('form').find('div').find('table')
for link in body:
    print(link.get_text())

# print(soup)

root = html.fromstring(page.content)
element = root.xpath('//html/body/div/div[2]/div[1]/div[4]/div[1]/h2')

print(type(print(element[0].text)))

tree = root.getroottree()
result = root.xpath('/html/body/div//*')

dom = etree.HTML(str(root))


def write_to_file(result):
    with open('xpaths.csv', 'w') as file:
        for r in result:
            xpath = tree.getpath(r)
            full_xpath = '/' + xpath
            elements = root.xpath(full_xpath)
            content_text = elements[0].text
            print(type(print(content_text)))
            if content_text is None or content_text == "" or len(content_text) == 0:
                content_text = str("None")
                file.write(content_text + ',')
                file.write(full_xpath)
            else:
                file.write(content_text + ',')
                file.write(full_xpath)
            file.write('\n')


if __name__ == '__main__':
    write_to_file(result)
