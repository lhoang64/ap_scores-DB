#!/usr/bin/env python3
"""
    desc: Main function, run to complete conversion, currently supports converting one year at a time
"""
import json
import os

from data.csv_json_converter import Record
from data.excel_cvs_converter import excel_to_csv

if __name__ == '__main__':
    # TODO: run converter on Male, and Female sheets

    excel_2017 = './final project data/2017'
    excel_2016 = './final project data/2016'
    excel_2015 = './final project data/2015'
    excel_2014 = './final project data/2014'
    csv_2017 = './final project data/csv/2017'
    csv_2016 = './final project data/csv/2016'
    csv_2015 = './final project data/csv/2015'
    csv_2014 = './final project data/2014'
    '''
    directories = {excel_2017: csv_2017, excel_2016: csv_2016, excel_2015: csv_2015, excel_2014: csv_2014}
    for key in directories:
        excel_to_csv('Female', key, directories[key])

    for d in os.listdir('./final project data/csv'):
        csv_path = os.path.join('./final project data/csv', d)
        for file in os.listdir(csv_path):
            file_path = os.path.join('./final project data/csv', d, file)

            new_record = Record(d, 'Computer Science A', file_path)
            new_record.set_scores()
            json_output_file = file.split('.')[0] + '.json'
            json_output_path = os.path.join('./final project data/json_files', json_output_file)
            print('Creating file: {}'.format(json_output_file))
            with open(json_output_path, 'w+') as json_file:
                json.dump(new_record.to_dict(), json_file)
    '''
    states = ['Missouri', 'Alaska', 'New Hampshire', 'Illinois', 'Virginia', 'Washington', 'Vermont', 'South Dakota',
              'Georgia', 'Connecticut', 'Alabama', 'Oklahoma', 'Colorado', 'Ohio', 'Maine', 'Mississippi', 'Utah',
              'South Carolina', 'Delaware', 'Indiana', 'Arkansas', 'Iowa', 'New Jersey', 'Wisconsin', 'Michigan',
              'Arizona', 'Massachusetts', 'Montana', 'New York', 'Wyoming', 'Minnesota', 'West Virginia', 'North Dakota',
              'Florida', 'DC', 'Kentucky', 'Louisiana', 'Maryland', 'Texas', 'Hawaii', 'Rhode Island', 'Kansas',
              'Pennsylvania', 'North Carolina', 'Nebraska', 'Tennessee', 'Idaho', 'Oregon', 'Nevada', 'California',
              'New Mexico']
    for state in states:
        files = [f for f in os.listdir(os.path.join('./final project data/json_files_female', state))]
        for file in files:
            with open(os.path.join('./final project data/json_files', state, file), 'r') as f:
                record = json.load(f)
                record['state'] = state
                with open('ap_scores_female.json', 'a') as final_output:
                    final_output.write(json.dumps(record) + '\n')

