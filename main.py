from bs4 import BeautifulSoup
from lxml import html, etree
from page_info import page

# --------SOUP-----------
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='news').find('table', id="kainos").find_all('td')
# print(results)
# body = BeautifulSoup('<a class="pointer" href="http://www.degalukainos.lt" title="Degalų kainos Lietuvoje" xpath="1"><img src="/img/logo_2.gif" width="142" height="62" alt="logo"></a>','html.parser')
# body = soup.find('body').find_all('img')
# for link in body:
# print(link.get_text())
# print(link)
# print(link.img['alt'])
# print(soup)

# -------LXML-----------
root = html.fromstring(page.content)
# element = root.xpath('/html/body/div[1]/div[4]/div[2]/p[1]')
# elementy = ('//html/body/div/div[2]/div[2]/div/form/div/div[2]/table/tr[2]/td[10]/div[1]/img')
# last=elementy.split('/')
# print(last[-1])
# print(element)
# print(element[0].text)
# print(type(print(element[0].text)))
tree = root.getroottree()


# results = root.xpath('/html/body/div//*')
# dom = etree.HTML(str(root))
# elementr = root.xpath('//html/body/div[1]/div[1]/div[1]/a')
# if elementr[0].get('href') is not None:
#     print(elementr[0].get('href'))
# else:
#     print('no')
#
# if elementr[0].get('id') is True:
#     print(elementr[0].get('id'))


# --------------------------------
# TODO 1) get id values (id='footCopy') where it is possible
# TODO 2) get href values (href=''http://www.degalukainos.lt/degalu-kainu-statistika?fuel_id=5) where it is possible
# TODO 3) JSON format like {'id': 'footCopy'} : /html/body/div/div[4]/div[2]s

def fetch_page_content():
    page_content = html.fromstring(page.content)
    return page_content


def fetch_root_tree(root):
    web_tree = root.getroottree()
    return web_tree


def fetch_web_element_info(root):
    web_elements = root.xpath('/html/body/div//*')
    return web_elements


def write_to_file(results, tree):
    with open('degaluKainos_xpaths.csv', 'w') as file:
        for result in results:
            xpath = tree.getpath(result)
            if not xpath.__contains__('script'):
                elements = root.xpath(xpath)
                content_text = elements[0].text
                last_elem = xpath.split('/')
                if last_elem[-1] == 'img':
                    atr_alt = elements[0].get('alt')
                    file.write("alt: " + atr_alt)
                elif last_elem[-1] == 'span':
                    elem_span = elements[0].get('class')
                    file.write('class: ' + elem_span)
                elif content_text is None or content_text.isspace():
                    # file.write("xpath " + xpath)
                    if elements[0].get('id') is not None:
                        atr_id = elements[0].get('id')
                        # file.write(elem_id)
                        file.write("id: " + atr_id)
                    elif elements[0].get('class') is not None:
                        atr_class = elements[0].get('class')
                        # file.write(elem_class)
                        file.write("class: " + atr_class)
                    elif elements[0].get('href') is not None:
                        atr_href = elements[0].get('href')
                        file.write("href: " + atr_href)
                    else:
                        file.write("No info (type: None)")
                # elif content_text.isspace():
                #     file.write('Empty Label Element: ' + last_elem[-1])
                else:
                    file.write("Text: " + content_text)
                file.write("," + "/" + xpath + "\n")


def write_to_json():
    pass


if __name__ == '__main__':
    root = fetch_page_content()
    tree = fetch_root_tree(root)
    results = fetch_web_element_info(root)
    write_to_file(results, tree)

    # xpathr = [tree.getpath(result) for result in results]
    # print(xpathr)
    # full_xpath = ['/' + xpathr[results.index(result)] for result in results]
    # print(full_xpath)
