my_dict = {'Ilya': 1996} # работа со словарями
print(my_dict) # работа со словарями
print(my_dict.get('Ilya')) # работа со словарями
print(my_dict.get('Jmix')) # работа со словарями
my_dict.update({'Max': 2003, 'Lui': 2008}) # работа со словарями
print(my_dict) # работа со словарями
my_dict.pop('Max') # работа со словарями
print(my_dict) # работа со словарями

my_set = {2, 2, 4, 4, 1, 1, 99, 99}
print(my_set)
my_set.add(34)
my_set.add(23)
print(my_set)
my_set.discard(3)
print(my_set)
my_set.discard(4)
print(my_set)