user_input = input("Please enter your desired text: ")
limited_input = user_input
if len(user_input) > 10 : limited_input = user_input[0:10] + "..."
print(limited_input)

# or
# user_input = input("Please enter your desired text: ")
# print(user_input[:10])
# if len(user_input) > 10: print("...")