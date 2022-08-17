import csv
from lxml import html
from page_info import page
import json


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
# root = html.fromstring(page.content)
# element = root.xpath('/html/body/div[1]/div[4]/div[2]/p[1]')
# elementy = ('//html/body/div/div[2]/div[2]/div/form/div/div[2]/table/tr[2]/td[10]/div[1]/img')
# last=elementy.split('/')
# print(last[-1])
# print(element)
# print(element[0].text)
# print(type(print(element[0].text)))
# tree = root.getroottree()

# results = root.xpath('/html/body/div//*')
# dom = etree.HTML(str(root))
# elementr = root.xpath('//html/body/div[1]/div[1]/div[1]/a')
# if elementr[0].get('href') is not None:
#     print(elementr[0].get('href'))
# else:
#     print('no')
# if elementr[0].get('id') is True:
#     print(elementr[0].get('id'))
# --------------------------------

def fetch_page_content():
    page_content = html.fromstring(page.content)
    return page_content


def fetch_root_tree(root):
    web_html_tree = root.getroottree()
    return web_html_tree


def fetch_web_element_info(root):
    web_elements = root.xpath('/html/body/div//*')
    return web_elements


def write_to_csv(results, tree, root):
    with open('outputs/Kainos_CSV_xpaths.csv', 'w', encoding='windows-1257', errors="xmlcharrefreplace") as file:
        file.write("type" + "," + "attribute" + "," + "xpath" + "\n")
        for result in results:
            xpath = tree.getpath(result)
            if not xpath.__contains__('script'):
                elements = root.xpath(xpath)
                content_text = elements[0].text
                if content_text is None or content_text.isspace():
                    if elements[0].get('id') is not None:
                        atr_id = elements[0].get('id')
                        file.write("id" + "," + atr_id)
                    elif elements[0].get('alt') is not None:
                        atr_alt = elements[0].get('alt')
                        file.write("alt" + "," + atr_alt)
                    elif elements[0].get('class') is not None:
                        atr_class = elements[0].get('class')
                        file.write("class" + "," + atr_class)
                    elif elements[0].get('href') is not None:
                        atr_href = elements[0].get('href')
                        file.write("href" + "," + atr_href)
                    else:
                        file.write("none" + "," + "")
                else:
                    file.write("text" + "," + content_text)
                file.write("," + "/" + xpath + "\n")


# add = {'type': 'ids',
#         'attribute': 'foot',
#         'xpath': '//html/body/div/*'}
#
# attributes = {'type': 'type',
#                'attribute': 'attribute',
#                'xpath': 'xpath'}
#
# json_load_add = json.dumps(add, indent=4)
# json_load_attribute = json.dumps(attributes, indent=4)
#
# print(json_load_add)
# print(json_load_attribute)
#
# json_merged={key:value for (key,value) in (add.items()+attributes.items())}
# my_dict = json.loads(json_merged)


def write_to_json():
    json_array = []
    with open('outputs/Kainos_CSV_xpaths.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)
    with open('outputs/Kainos_JSON_xpaths.json', 'w') as json_file:
        json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
        json_file.write(json_string)


if __name__ == '__main__':
    web_root = fetch_page_content()
    web_tree = fetch_root_tree(web_root)
    web_results = fetch_web_element_info(web_root)
    write_to_csv(web_results, web_tree, web_root)
    write_to_json()

    # xpathr = [tree.getpath(result) for result in results]
    # print(xpathr)
    # full_xpath = ['/' + xpathr[results.index(result)] for result in results]
    # print(full_xpath)
