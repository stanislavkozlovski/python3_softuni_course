prices = []
sum_of_prices = 0

with open("/home/netherblood/Downloads/Python/find_average_price_from_file/catalog_full.csv", 'r', encoding="utf-8") as sample:
    for line in sample:
        product_info = line.split(',')
        product_price = float(product_info[-1])
        prices.append(product_price)
        sum_of_prices += product_price

average_price = sum_of_prices/len(prices)  # no need to iterate the list again with sum(prices)
#  average_price = sum(prices)/len(prices)
print("Average price is {}".format(average_price))