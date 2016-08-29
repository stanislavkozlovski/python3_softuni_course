# prints the whole expected output
def print_results(number_of_sales, sum_of_sales, average_sale, latest_sale_date, earliest_sale_date, top_five_category,
                  top_five_city, top_five_date):

    print_totals(number_of_sales,sum_of_sales,average_sale,earliest_sale_date,latest_sale_date)
    print_top5_categories(top_five_category)
    print_top5_cities(top_five_city)
    print_top5_dates(top_five_date)


def print_totals(number_of_sales, sum_of_sales, average_sale, earliest_sale_date, latest_sale_date):
        print("""Обобщение
---------
Общ брой продажби: {0}
Общо сума продажби: {1:.2f} €
Средна цена на продажба: {2:.2f} €
Начало на период на данните: {3}
Край на период на данните: {4}
    """.format(number_of_sales, sum_of_sales, average_sale, earliest_sale_date, latest_sale_date))


def print_top5_categories(top_five_category):

    print("""Сума на продажби по категории (top 5)
-----------------------------""")
    for category, category_sum in top_five_category:
        print("    {0}: {1:.2f} €".format(category, category_sum))


def print_top5_cities(top_five_city):
    print("""Сума на продажби по градове (top 5)
-----------------------------""")
    for city, city_sum in top_five_city:
        print("    {0}: {1:.2f} €".format(city, city_sum))


def print_top5_dates(top_five_date):
    print("""Сума на продажби по час (top 5)
-----------------------------""")
    for date, date_sum in top_five_date:
        print("    {0}: {1:.2f} €".format(date, date_sum))
