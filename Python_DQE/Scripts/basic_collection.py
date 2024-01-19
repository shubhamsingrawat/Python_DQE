"""
Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.

"""

#1. create a list of random number of dicts (from 2 to 10)
import random
from collections import defaultdict
# getting the random number to genrate the list of dict
rand_num = random.randint(2, 10)

print(rand_num)
list_dict = []
while rand_num > 0:
    temp_tuple = {chr(random.randint(ord('a'),ord('z'))):random.randint(0,100) for _ in range(0,3)}
    list_dict.append(temp_tuple)
    #print(temp_tuple)
    rand_num -= 1

print(list_dict)

#2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# list_dict = [{'a': 28, 'v': 13, 'e': 21}, {'y': 14, 'd': 17, 'c': 62}, 
#              {'o': 23, 'k': 11, 'u': 100}, {'v': 29, 'a': 1, 'r': 58}]

# creating a dict with list as value holding (ind_dict, value_for_chr)
check = defaultdict(list)
for idx,dict_items in enumerate(list_dict):
    for key , value in dict_items.items():
        check[key].append((idx,value))

print(check)

# final dict with max value and rename key with dict number with max value
final_dict = {}
for key, val_list in check.items():
    if len(val_list) == 1:
        final_dict[key] = val_list[0][1] # getting value from list e.g [0,9] --> 9
    else:
        max_value = max(val_list, key=lambda item:item[1]) # e.g 'i': [(6, 38), (7, 28)]
        new_key = key+"_"+str(max_value[0])
        final_dict[new_key] = max_value[1]

print(final_dict)