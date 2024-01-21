import csv
import os
from collections import defaultdict

"""
Create two csv:
1.word-count (all words are preprocessed in lowercase)
"""
def genrate_word_dict():
    dict_var = defaultdict(int)
    res_list = []
    with open(r"Reports_data.txt",'r') as file:
        res_list = file.readlines()

    for line in res_list:
        for word in line.strip().split(" "):
            dict_var[word.lower()] += 1
    return dict_var

def genrate_csv(dict_var):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key, val in dict_var.items():
            writer.writerow({'word': key, 'count': val})

if __name__ == '__main__':
    res_dict = genrate_word_dict()
    print(res_dict)
    genrate_csv(res_dict)
