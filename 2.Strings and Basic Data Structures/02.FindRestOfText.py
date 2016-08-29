user_input = input()
find_keyword = input()
text_partition = user_input.partition(find_keyword) # [0] is the part of the text before the keyword, [1] is they keyword and [2] is the text after the keyword

if(text_partition[2] == ''): #has not been found
    print(user_input)
else:
    print(text_partition[2]) #prints the part of the text after the keyword
