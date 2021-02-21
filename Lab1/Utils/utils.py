import requests
from lxml import html


def receive_html_by_url(url: str):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    return html.fromstring(response.text)


def normalize_string_array(array):
    result_arr = []
    for string in array:
        tmp_string = str(string).replace("\n", "").replace("\t", "").replace("\r", "")
        tmp_string = tmp_string.strip()
        if len(tmp_string) > 0 and is_appropriate_char(tmp_string):
            result_arr.append(tmp_string)
    return result_arr


def filter_conditions(variable):
    return not (variable == "" or variable == " ")


def normalize_array(array):
    return list(filter(filter_conditions, array))


def delete_duplicates(array):
    return list(dict.fromkeys(array))


def normalize_link_array(link_array, url_arr):
    result_arr = []
    for link_ in link_array:
        for url_ in url_arr:
            if str(link_).startswith(url_) and str(link_) != url_:
                result_arr.append(link_)
                break
    return delete_duplicates(result_arr)[:20]


def is_appropriate_char(string):
    return not (len(string) == 1 and not string.isalpha())


def get_text_arr_from_html(html_):
    return html_.xpath('body//*[not(self::script or self::style or self::img)]/text()')


def get_link_arr_from_html(html_):
    return html_.xpath('//a/@href')


def get_img_link_arr_from_html(html_):
    return html_.xpath('//img/@src')


