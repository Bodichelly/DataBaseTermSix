from Utils import xmlutils


def perform_fourth_task():
    tree = xmlutils.parse_xml("task_three_result.xml")
    xslt = xmlutils.parse_xml("task_four.xsl")
    transformed_xslt = xmlutils.transform_xslt(xslt)
    html = transformed_xslt(tree)
    html.write('task_four_result.html', pretty_print=True, xml_declaration=True, encoding="utf-8")
