from Utils import utils, xmlutils
from xml.dom import minidom


class Product:
    def __init__(self, name, price, description, photo_url):
        self.name= name
        self.description = description
        self.photo_url = photo_url
        self.price = price


def perform_third_task():

    url = 'https://allo.ua/'

    html = utils.receive_html_by_url(url)
    product_links = html.xpath("//a[contains(@class, 'h-pc__img-link')]/@href")[:20]
    product_arr = []
    for link in product_links:
        product_arr.append(get_product_data(link))
    root = minidom.Document()
    data = root.createElement('data')
    xmlutils.insert_element(root, data)

    for product in product_arr:
        try:
            product_node = root.createElement("product")
            xmlutils.insert_element(product_node, xmlutils.create_text_element(root, "title", product.name))
            xmlutils.insert_element(product_node, xmlutils.create_text_element(root, "image", product.photo_url))
            xmlutils.insert_element(product_node, xmlutils.create_text_element(root, "price", product.price))
            xmlutils.insert_element(product_node, xmlutils.create_text_element(root, "description", product.description))
            xmlutils.insert_element(data, product_node)
        except Exception as E:
            print(E)
            continue
    with open('task_three_result.xml', 'w', encoding="utf-8") as f:
        f.write(root.toprettyxml())


def get_product_data(url):
    html = utils.receive_html_by_url(url)
    product_name = html.xpath("//h1[contains(@class, 'product-header__title')]/text()")[0]
    photo_url = html.xpath("//img[contains(@class, 'main-gallery__image')]/@data-src")[0]
    price = html.xpath("//span[contains(@class, 'sum')]/text()")[0]
    if len(price) == 0:
        price = "Немає в наявності"
    description = html.xpath("//p[contains(@class, 'text_general')]/text() | //p[contains(@class, 'l-paragraph')]/text() | //div[contains(@class, 'product-cms__short-description-content')]/text()")
    description = utils.normalize_string_array(description)
    description = "".join(description)
    return Product(product_name, price, description, photo_url)
