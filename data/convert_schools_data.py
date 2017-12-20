#!/usr/bin/env python3

import csv
import json

def convert_schools_data(input_path, output_path):
    rows = []
    output = {} # {'2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0,
              #'2017': 0}
    with open(input_path, 'r') as input_file:
        c = csv.reader(input_file)
        for r in c:
            rows.append(r)
    for i in range(1, 11):
        output[rows[0][i]] = rows[10][i]
    with open(output_path, 'w') as output_file:
        json.dump(output, output_file)

input_path = './final project data/schools.csv'
output_path = './final project data/schools.json'
convert_schools_data(input_path, output_path)
