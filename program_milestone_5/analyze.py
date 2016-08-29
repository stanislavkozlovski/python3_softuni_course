"""
A program that analyzes the sales from a pre-made sales.csv file and catalog.csv
Sample Command: python3 analyze.py /home/user/downloads/catalog.csv /home/user/downloads/sales-1M.csv

Old solution is commented out in favor of an OOP approach
"""

import os
import sys
import iso8601
import pytz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #needed to have it work from the console
from sys import argv
from datetime import datetime, MAXYEAR, MINYEAR
from collections import Counter
from program_milestone_5.sales import read_sales, KEY_CITY, KEY_PRICE, KEY_DATE_STR, KEY_PRODUCT_CATEGORY
# from program_milestone_5.analysis_printer import print_results NOT USED ANYMORE
from program_milestone_5.catalog import read_catalog


if len(argv) < 3:
    print("I need two arguments, the path to the catalog and sales .csv files!")
    exit()
PATH_TO_CATALOG = argv[1]
PATH_TO_SALES_FILE = argv[2]

def main():
    ID_group_dict = read_catalog(PATH_TO_CATALOG)  #dictionary that has a group as key and the products that are in said group in a set
    # total_sum, sales_count = 0, 0
    #
    # utc = pytz.utc
    # earliest_sale_date = datetime(MAXYEAR, 1, 1)  # placeholder, should be replaced in first iteration
    # earliest_sale_date = utc.localize(earliest_sale_date)
    # latest_sale_date = datetime(MINYEAR, 1, 1)  # placeholder, should be replaced in first iteration
    # latest_sale_date = utc.localize(latest_sale_date)
    #
    # #  dictionaries to hold the sales and eventually to have the top 5 be extracted from them
    # # key: group,date or city ; value: the sum of money generated from said key
    # group_sales_sum_dict , date_sales_sum_dict, city_sales_sum_dict = {}, {}, {}

    totals_analyzer = TotalsAnalyzer()
    group_analyzer = CategoriesAnalyzer()
    city_analyzer = CitiesAnalyzer()
    date_analyzer = DateAnalyzer()

    print('Analyzing...')
    for sale in read_sales(PATH_TO_SALES_FILE, ID_group_dict):

        totals_analyzer.analyze(sale)
        group_analyzer.analyze(sale)
        city_analyzer.analyze(sale)
        date_analyzer.analyze(sale)

        # sale_price = sale[KEY_PRICE]
        # sale_city = sale[KEY_CITY]
        # sale_product_group = sale[KEY_PRODUCT_CATEGORY]
        #
        #
        # totals_analyzer.analyze(sale)
        # sales_count += 1
        # total_sum += sale_price
        #
        # # configure the date and check if it's the earliest/latest
        # sale_date = iso8601.parse_date(sale[KEY_DATE_STR].replace('"', ''))
        # original_tz = sale_date.tzinfo  # we will convert it back later
        # sale_date = sale_date.astimezone(utc)  # convert to UTC
        # if sale_date < earliest_sale_date:
        #     earliest_sale_date = sale_date
        # if sale_date > latest_sale_date:
        #     latest_sale_date = sale_date
        #
        # # update the dictionary holding the top 5 dates
        # sale_date = sale_date.astimezone(original_tz).replace(minute=0, second=0, microsecond=0)
        # date_sales_sum_dict[sale_date] = date_sales_sum_dict.get(sale_date, 0) + sale_price
        #
        # # update the dictionary holding the cities with the top 5 sales
        # city_sales_sum_dict[sale_city] = city_sales_sum_dict.get(sale_city, 0) + sale_price
        #
        # # update the dictionary holding the categories with the top 5 sales
        # group_sales_sum_dict[sale_product_group] = group_sales_sum_dict.get(sale_product_group, 0) + sale_price


    totals_analyzer.print_results()
    group_analyzer.print_results()
    city_analyzer.print_results()
    date_analyzer.print_results()
    # top_five_group_sales = get_top5_sales(group_sales_sum_dict)
    # top_five_city_sales = get_top5_sales(city_sales_sum_dict)
    # top_five_date_sales = get_top5_sales(date_sales_sum_dict)
    #
    # print_results(number_of_sales = sales_count,
    #               sum_of_sales = total_sum,
    #               average_sale = total_sum/sales_count if sales_count else None,
    #               latest_sale_date = datetime.isoformat(latest_sale_date),
    #               earliest_sale_date = datetime.isoformat(earliest_sale_date),
    #               top_five_group=top_five_group_sales,
    #               top_five_city=top_five_city_sales,
    #               top_five_date=top_five_date_sales)


class BaseAnalyzer:
    def analyze(self, sale: dict):
        pass

    def print_results(self):
        pass


class GroupedAnalyzer(BaseAnalyzer):
    group_bg_str = ''
    def __init__(self):
        self._sum_dictionary = {}

    def analyze(self, sale: dict):
        self._sale_price = sale[KEY_PRICE]
        self._group_value = self.get_group_by_value(sale)

        self._sum_dictionary[self._group_value] = self._sum_dictionary.get(self._group_value, 0) \
                                                  + self._sale_price

    # return a list of tuples(key,value) with the top 5 sales in a given dictionary
    def get_top5_sales(self, sales_dictionary: dict) -> list:
        """
        Result sample:
        [(SHOES,15042.34),
         (MANCHESTER, 4392.3),
         (2015-04-23-14:00:00:00, 415,4)
        ]
        """
        return Counter(sales_dictionary).most_common(5)

    def get_group_by_value(self, sale: dict):
        pass

    def print_results(self):
        self._top_five = self.get_top5_sales(self._sum_dictionary)
        print("""Сума на продажби по {} (top 5)
    -----------------------------""".format(self.group_bg_str))

        for group, group_sum in self._top_five:
            print("    {0}: {1:.2f} €".format(group, group_sum))


class TotalsAnalyzer(BaseAnalyzer):
    def __init__(self):
        self._utc = pytz.utc
        self._sale_count = 0
        self._sales_sum = 0
        self._sale_average = 0

        self._earliest_sale_date = datetime(MAXYEAR, 1, 1)  # placeholder, should be replaced in first iteration
        self._earliest_sale_date = self._utc.localize(self._earliest_sale_date)

        self._latest_sale_date = datetime(MINYEAR, 1, 1)  # placeholder, should be replaced in first iteration
        self._latest_sale_date = self._utc.localize(self._latest_sale_date)

    def analyze(self, sale: dict):
        self._sale_price = sale[KEY_PRICE]

        self._sale_count += 1
        self._sales_sum += self._sale_price

        # configure the date and check if it's the earliest/latest
        self._sale_date = iso8601.parse_date(sale[KEY_DATE_STR].replace('"', ''))
        self._sale_date = self._sale_date.astimezone(self._utc)  # convert to UTC

        if self._sale_date < self._earliest_sale_date:
            self._earliest_sale_date = self._sale_date
        if self._sale_date > self._latest_sale_date:
            self._latest_sale_date = self._sale_date

    def print_results(self):
        self._sale_average = self._sales_sum/self._sale_count
        print("""Обобщение
---------
Общ брой продажби: {0}
Общо сума продажби: {1:.2f} €
Средна цена на продажба: {2:.2f} €
Начало на период на данните: {3}
Край на период на данните: {4}
    """.format(self._sale_count, self._sales_sum, self._sale_average, self._earliest_sale_date, self._latest_sale_date))


class CategoriesAnalyzer(GroupedAnalyzer):
    group_bg_str = 'категории'
    def get_group_by_value(self, sale: dict):
            return sale[KEY_PRODUCT_CATEGORY]


class CitiesAnalyzer(GroupedAnalyzer):
    group_bg_str = 'градове'
    def get_group_by_value(self, sale: dict):
            return sale[KEY_CITY]


class DateAnalyzer(GroupedAnalyzer):
    group_bg_str = 'час'
    def get_group_by_value(self, sale: dict):
        return iso8601.parse_date(sale[KEY_DATE_STR].replace('"', '')).replace(minute=0, second=0, microsecond=0)



if __name__ == "__main__":
    main()
