prices = dict()
sum_of_prices = 0
file_dir = "/home/netherblood/Downloads/Python/find_average_price_from_file/catalog_full.csv"
newfile_dir = "/home/netherblood/Downloads/Python/find_average_price_from_file/catalog_full_raised_prices.csv"

with open(file_dir, 'r', encoding="utf-8") as catalog:
    with open(newfile_dir, 'w', encoding="utf-8") as catalog_raised_prices:
        for line in catalog:
            product_info = line.split(',')

            old_price = float(product_info[-1])
            new_price = old_price + old_price * 0.75

            # replace from index to make suer we don't replace anything else
            index_of_old_price = len(line)-len(str(old_price)) - 1
            updated_line = line[:index_of_old_price] + line[index_of_old_price:].replace(str(old_price), str(new_price))

            catalog_raised_prices.write(updated_line)