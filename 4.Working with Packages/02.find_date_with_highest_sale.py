import iso8601


def import_information_to_dict() -> dict:
    sales_dict = {}
    with open("/home/netherblood/Downloads/Python/find_time_with_highest_sales/sales.csv", "r") as sales_file:
        for line in sales_file:
            sale_info = line.split(',')
            date_of_sale = iso8601.parse_date(sale_info[0]).replace(minute=0, second=0, microsecond=0)
            price_of_sale = float(sale_info[1])

            sales_dict[date_of_sale] = sales_dict.get(date_of_sale, 0) + price_of_sale
    return sales_dict

sales = import_information_to_dict()

print(max(sales))
print(sales[max(sales)])