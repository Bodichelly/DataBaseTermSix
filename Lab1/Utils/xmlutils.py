# import xml.etree.ElementTree as ElementTree
import lxml.etree as ElementTree


def parse_xml(url):
    return ElementTree.parse(url)


def transform_xslt(xslt):
    return ElementTree.XSLT(xslt)


def create_element(root, name, attr_name, attr_data):
    created_element = root.createElement(name)
    created_element.setAttribute(attr_name, attr_data)
    return created_element


def create_text_element(root, name, text):
    created_element = root.createElement(name)
    text_node = root.createTextNode(text)
    created_element.appendChild(text_node)
    return created_element


def insert_element(parent, child):
    parent.appendChild(child)
