from Utils import utils, xmlutils


def perform_second_task():
    tree = xmlutils.parse_xml("task_one_result.xml")
    page_array = tree.findall(".//page")
    images_sum = 0
    page_number = 0
    for page in page_array:
        try:
            images_sum += len(page.findall(".//image"))
            page_number += 1
        except:
            continue
    print("Середня кількість графічних фрагментів "+ str((images_sum/page_number).__floor__()))

