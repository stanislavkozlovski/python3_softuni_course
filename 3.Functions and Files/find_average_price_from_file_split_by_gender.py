prices = dict()
sum_of_prices = 0
file_dir = "/home/netherblood/Downloads/Python/find_average_price_from_file/catalog_full.csv"

with open(file_dir, 'r', encoding="utf-8") as file:
    for line in file:
        product_info = line.split(',')
        product_price = float(product_info[-1])
        product_gender = product_info[-2]

        if product_gender not in prices: # create the key
            prices[product_gender] = product_price, 1

        gender_sum, gender_num_products = prices[product_gender]
        gender_sum += product_price
        gender_num_products += 1
        prices[product_gender] = gender_sum, gender_num_products


for gender in prices:
    sum, number_of_products = prices[gender]
    average_price = sum/number_of_products

    print("Average price for {} products is {:.2f}".format(gender, average_price))