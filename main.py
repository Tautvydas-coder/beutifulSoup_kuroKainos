import requests
from bs4 import BeautifulSoup
from lxml import html, etree

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}
page = requests.get(url='http://www.degalukainos.lt', headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='news').find('table', id="kainos").find_all('td')
# print(results)
# body = BeautifulSoup('<a class="pointer" href="http://www.degalukainos.lt" title="Degalų kainos Lietuvoje" xpath="1"><img src="/img/logo_2.gif" width="142" height="62" alt="logo"></a>','html.parser')
# body = soup.find('body').find_all('div')
# for link in body:
#     print(link.get_text())
#     print(link)
#     print(link.img['alt'])

# print(soup)

root = html.fromstring(page.content)
element = root.xpath('//html/body/div/div[2]/div[2]/div/form/div/div[2]/table/tr[2]/td[10]/div[1]/img')
elementy = ('//html/body/div/div[2]/div[2]/div/form/div/div[2]/table/tr[2]/td[10]/div[1]/img')
# last=elementy.split('/')
# print(last[-1])
# print(element)
# print(element[0].attrib['title'])
# print(type(print(element[0].text)))

tree = root.getroottree()
result = root.xpath('/html/body/div//*')

dom = etree.HTML(str(root))


# elementr = root.xpath('//html/body/div[1]/div[2]/div[2]/div/form/div/div[2]/table')
# print(elementr[0].attrib['id'])

def write_to_file(result):
    with open('xpaths.csv', 'w') as file:
        for r in result:
            xpath = tree.getpath(r)
            full_xpath = '/' + xpath
            if not (full_xpath.__contains__('script') or full_xpath.__contains__('plusone') or full_xpath.__contains__(
                    'ins')):
                elements = root.xpath(full_xpath)
                # print(full_xpath)
                content_text = elements[0].text
                print(content_text)

                # print(type(print(content_text)))
                last_elem = xpath.split('/')
                # print(last_elem[-1])
                if last_elem[-1] == 'img':
                    elem_title = elements[0].attrib['alt']
                    file.write(elem_title + ',')
                    file.write(full_xpath)
                elif last_elem[-1] == 'table':
                    file.write('Table' + ',')
                    file.write(full_xpath)
                elif last_elem[-1] == 'span':
                    elem_title = elements[0].attrib['class']
                    file.write('Class name: ' + elem_title + ',')
                    file.write(full_xpath)
                elif last_elem[-1] == '':
                    elem_title = elements[0].attrib['']
                    file.write('Element: ' + elem_title + ',')
                    file.write(full_xpath)
                elif content_text is None:
                    file.write(str("Label Element ") + last_elem[-1] + ',')
                    file.write(full_xpath)
                elif content_text.isspace():
                    file.write('Empty Label Element ' + last_elem[-1] + ',')
                    file.write(full_xpath)
                else:
                    file.write(content_text + ',')
                    file.write(full_xpath)
                file.write('\n')


if __name__ == '__main__':
    write_to_file(result)
