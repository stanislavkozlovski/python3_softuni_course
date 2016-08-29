ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

print("Their mutual interests are: ")
for interest in set(ivan).intersection(set(maria)): #cast the lists into a set to use the .intersection function
    print(interest, end=' ')