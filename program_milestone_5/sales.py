import csv
COLUMN_SALE_ID = 0
COLUMN_SALE_CITY = 2
COLUMN_SALE_DATE = 3
COLUMN_SALE_PRICE = 4  # last one

KEY_PRODUCT_CATEGORY = 'product_category'
KEY_CITY = 'city'
KEY_DATE_STR = 'date_str'
KEY_PRICE = 'price'


#  you put in the product ID number and this returns its category
def get_category(ID_category_dict: dict, product_ID) -> str:
    #  used to fill in the dictionary with the top 5 category sales
    
    for key in ID_category_dict:
        if product_ID in ID_category_dict[key]:
            return key

    raise FileNotFoundError("Could not find the product_ID")


# read the file line by line and return information with said line each time
def read_sales(PATH_TO_SALES_FILE, ID_category_dict):

    with open(PATH_TO_SALES_FILE, 'r', encoding="utf-8") as csvfile:
        sales_reader = csv.reader(csvfile)

        for sales_line_info in sales_reader:
            sale = {}

           # sales_line_info = sales_line_info.split(',')
            sale_product_ID = sales_line_info[COLUMN_SALE_ID]  # used only here to get the proper category, no need to return it
            sale[KEY_PRODUCT_CATEGORY] = get_category(ID_category_dict, sale_product_ID)
            sale[KEY_CITY] = sales_line_info[COLUMN_SALE_CITY]
            sale[KEY_DATE_STR] = sales_line_info[COLUMN_SALE_DATE]
            sale[KEY_PRICE] = float(sales_line_info[COLUMN_SALE_PRICE])

            yield sale


