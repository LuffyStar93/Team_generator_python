#!/usr/bin/env python3


import datetime
import random
import sys
import json


myfile = open(sys.argv[1],'r')
nbr_by_group = int(sys.argv[2])
info = myfile.readlines()
# print(info)
my_list = info[0].replace('\n', '').split(', ')
nbr_student = len(my_list)
i = 0
default_data = {}
# teams = [students[i:i+3] for i in range(0, nbr_student, nbr_by_group)]
# print(teams)


def create_groups(students, nbr_by_group):
        random.shuffle(my_list)
        groups = [students[i:i+nbr_by_group] for i in range(0, nbr_student, nbr_by_group)]
        # default_data = {}
        # print('groups', groups)
        # print(groups)
        
        for group in groups:
           
            # print(group)
            default_data[groups.index(group)] = group 
            # default_data.update({i+1 : group})
            # print('default = ', default_data)
        return default_data

default_data = create_groups(my_list, nbr_by_group)
print('default=',default_data)

with open('result.json', 'w') as fp:
    json.dump(default_data, fp, indent=4)