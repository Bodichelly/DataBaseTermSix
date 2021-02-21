from Utils import utils, xmlutils
from xml.dom import minidom


def perform_first_task():
    url = 'http://www.ua.igotoworld.com'
    alter_url = 'https://ua.igotoworld.com'

    html = utils.receive_html_by_url(url)
    link_arr = utils.get_link_arr_from_html(html)
    link_arr = utils.normalize_link_array(link_arr, [url, alter_url])

    root = minidom.Document()
    data = root.createElement('data')
    xmlutils.insert_element(root, data)

    for link_ in link_arr:
        try:
            current_html = utils.receive_html_by_url(link_)
            page_node = xmlutils.create_element(root, "page", "url", link_)
            text_arr = utils.get_text_arr_from_html(current_html)
            text_arr = utils.normalize_array(text_arr)
            text_arr = utils.normalize_string_array(text_arr)
            img_arr = utils.get_img_link_arr_from_html(current_html)
            img_arr = utils.normalize_array(img_arr)
            text_fragment = xmlutils.create_element(root, "fragment", "type", "text")
            img_fragment = xmlutils.create_element(root, "fragment", "type", "image")
            xmlutils.insert_element(page_node, text_fragment)
            xmlutils.insert_element(page_node, img_fragment)
        except Exception as E:
            print(E)
            continue

        for text_str in text_arr:
            text = xmlutils.create_text_element(root, "text", text_str)
            xmlutils.insert_element(text_fragment, text)
        for img_url in img_arr:
            img = xmlutils.create_text_element(root, "image", img_url)
            xmlutils.insert_element(img_fragment, img)
        xmlutils.insert_element(data, page_node)

    with open('task_one_result.xml', 'w', encoding="utf-8") as f:
        f.write(root.toprettyxml())
