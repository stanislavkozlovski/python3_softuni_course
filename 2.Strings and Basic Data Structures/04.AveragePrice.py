priceList = []

while(True):
    user_input = input("Enter a price (or 'stop'): ")
    if user_input == 'stop': break
    priceList.append(float(user_input))

# remove min and max prices
priceList.remove(max(priceList))
priceList.remove(min(priceList))

print("Average price is: {}".format(float(sum(priceList)/len(priceList))))