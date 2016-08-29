name = str(input("Enter your name: "))
name_list = name.split()
length = len(name_list)

if length > 0:
    for i in range(length): #iterate through the list
        current_initial = name_list[i][0] #first letter is the initial
        if current_initial.isupper(): #if it's in upper case it's most likely a name
            print("{0}.".format(current_initial), end='')

