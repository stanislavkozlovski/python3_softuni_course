"""
sample input: python3 find_sales_from_city.py ./database
"""
import sys
import sqlite3

if(len(sys.argv) < 2):
    print("You need to enter the path to the database!")
    exit()

PATH_TO_DB = sys.argv[1]

user_input_city = input("Въведете име на град: ")
output_list = []
with sqlite3.connect(PATH_TO_DB, isolation_level=None) as db_connection:
    cursor = db_connection.cursor()

    # get all the sales from that city from the database
    sales = cursor.execute("SELECT item_key, sale_timestamp, price FROM sale WHERE city_name = ?", [user_input_city])

# iterate through the sales and save them as a string in a list
for output_line in sales:
    sale_item_key = output_line[0]
    sale_timestamp = output_line[1]
    sale_price = float(output_line[2])
    output_list.append("Артикул #: {0}   дата/час: {1}  сума: {2:.2f}".format(sale_item_key, sale_timestamp, sale_price))

if len(output_list) == 0:  # check if we have any sales from said city
    print("Няма данни за продажби в град {}".format(user_input_city))
else:
    print("Продажби в град {}: ".format(user_input_city))
    print()
    for output_line in output_list:
        print(output_line)