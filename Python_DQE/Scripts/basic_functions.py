import random
from collections import defaultdict

#1 create list of 100 random numbers from 0 to 1000
def genrate_random(start: int = 0, end: int = 1000) -> list:
    arr = [random.randint(0,1000) for i in range(0,100)]
    return arr

#2 sort list from min to max (without using sort())
def sort_arr(arr: list) -> list:
    for i in range(0, len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

#3 calculate average for even and odd numbers
def avg_even_odd(arr:list)->tuple:
    """
    @param : arr list()
    @return tuple(odd_avg, even_avg)
    """
    even_elem, odd_elem = [], [] # holding even and odd elem
    for i in arr:
        even_elem.append(i) if i % 2 == 0 else odd_elem.append(i)

    even_avg = sum(even_elem)/len(even_elem)
    odd_avg = sum(odd_elem)/len(odd_elem)

    return (odd_avg, even_avg)


#4. create a list of random number of dicts (from 2 to 10)
def random_dict() -> dict:
    """
    this function genrate the list of dicts
    dict's random numbers of keys should be letter,
    dict's values should be a number (0-100),
    example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
    """
    # getting the random number to genrate the list of dict
    rand_num = random.randint(2, 10)
    print(rand_num)
    list_dict = []
    while rand_num > 0:
        temp_tuple = {chr(random.randint(ord('a'),ord('z'))):random.randint(0,100) for _ in range(0,3)}
        list_dict.append(temp_tuple)
        rand_num -= 1
    print("list_dict: ", list_dict)
    return list_dict

#4.1 creating a dict with list as value holding (ind_dict, value_for_chr)
def dict_keys_value(list_dict : dict ) -> dict:
    check = defaultdict(list)
    for idx,dict_items in enumerate(list_dict):
        for key , value in dict_items.items():
            check[key].append((idx,value))
    print("dict_key_value_list: ", check)
    return check

#5 : final dict with max value and rename key with dict number with max value
def dict_key_max_value() -> dict:
    final_dict = {} # holding results
    list_dict = random_dict() #4
    check = dict_keys_value(list_dict) #4.1
    for key, val_list in check.items():
        if len(val_list) == 1:
            final_dict[key] = val_list[0][1] # getting value from list e.g [0,9] --> 9
        else:
            max_value = max(val_list, key=lambda item:item[1]) # e.g 'i': [(6, 38), (7, 28)]
            new_key = key+"_"+str(max_value[0])
            final_dict[new_key] = max_value[1]

    return final_dict

if __name__ == '__main__':
    #1
    arr = genrate_random()
    print("random 100 elem: \t", arr)
    #2
    soreted_arr = sort_arr(arr)
    print("sorted 100 elem: \t", soreted_arr)
    #3
    res = avg_even_odd(soreted_arr)
    print("avg odd elem: \t", res[0])
    print("avg even elem: \t", res[1])

    #5
    final_dict = dict_key_max_value()
    print(final_dict)
    