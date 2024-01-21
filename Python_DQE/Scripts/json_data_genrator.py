import json
from collections import defaultdict

def genrate_word_dict():
    dict_var = defaultdict(int)
    res_list = []
    with open(r"Reports_data.txt",'r') as file:
        res_list = file.readlines()

    for line in res_list:
        for word in line.strip().split(" "):
            dict_var[word.lower()] += 1
    return dict_var

def genrate_json(data):
    with open("word_count.json",'w') as fileptr :
        json.dump(data, fileptr)

if __name__ == '__main__':
    report_dict = genrate_word_dict()
    print(json.dumps(report_dict))

    genrate_json(report_dict)
