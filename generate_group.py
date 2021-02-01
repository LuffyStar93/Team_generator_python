#!/usr/bin/env python3


import datetime
import random
import sys
import json
import logging


myfile = open(sys.argv[1],'r')
nbr_by_group = int(sys.argv[2])
info = myfile.readlines()
# print(info)
my_list = info[0].replace('\n', '').split(', ')
nbr_student = len(my_list)
i = 0
default_data = {}
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='info.log', encoding='utf-8', level=logging.DEBUG)



def create_groups(students, nbr_by_group):
        logging.warning('Start of Function')
        random.shuffle(my_list)
        groups = [students[i:i+nbr_by_group] for i in range(0, nbr_student, nbr_by_group)]
        
        logging.info('Generate groups')
        for group in groups:
            default_data[groups.index(group)] = group 
        return default_data

default_data = create_groups(my_list, nbr_by_group)

logging.info('Groups generate succesfully !')

print(default_data)

logging.info('Creation of result in json file')

with open('result.json', 'w') as fp:
    json.dump(default_data, fp, indent=4)

logging.info('File generated succesfully !')