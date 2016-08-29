"""
    Expected catalog columns:
        1.Идентификационен номер на артикула;
        2.Наименование на артикула;
        3.Цветове, в които артикулът е наличен;
        4.Група на артикула;
        5.Спорт, за който е предназначен артикулът;
        6.Категория
        7.Подкатегория
        8.Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета
"""
import csv

COLUMN_PRODUCT_ID = 0
COLUMN_PRODUCT_CATEGORY = 5

#  create dictionaries using keys as the product category and values as sets that hold all the unique product numbers
def read_catalog(PATH_TO_CATALOG) -> dict:
    """
    ID_category_dict:
    {
        # category name: set of item ids
        "SHOES": ["J11382", "2314D"]
        ...
    }
    """
    ID_category_dict = {}

    with open(PATH_TO_CATALOG, 'r', encoding="utf-8") as csv_catalog_file:
        catalog_reader = csv.reader(csv_catalog_file)

        for catalog_line_info in catalog_reader:

            product_ID = catalog_line_info[COLUMN_PRODUCT_ID]
            product_category = catalog_line_info[COLUMN_PRODUCT_CATEGORY]

            if product_category not in ID_category_dict:
                ID_category_dict[product_category] = set()

            ID_category_dict[product_category].add(product_ID)

    return ID_category_dict
