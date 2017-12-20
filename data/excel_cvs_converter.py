#!/usr/bin/env python3
"""
    desc: Function used to convert source excel sheets into csv files
          Uses the openpyxl library by Eric Gazoni and Charlie Clark to open and read .xlsx files
    author: Linh Hoang <lhoang@bennington.edu>
    date: 12/5/17
"""

import openpyxl
import csv
import os


def excel_to_csv(sh_name, input_directory, output_dir):
    files = os.listdir(input_directory)
    for file in files:
        if file.endswith('xlsx'):
            try:
                file_path = os.path.join(input_directory, file)
                wb = openpyxl.load_workbook(file_path)
                sh = wb.get_sheet_by_name(sh_name)
                csv_file_name = '{0}-{1}.csv'.format(sh_name, file.split('.')[0])
                output_path = os.path.join(output_dir, csv_file_name)
                sh_content = []
                for r in sh:
                    sh_content.append([cell.value for cell in r])
                print('Creating file: {}'.format(csv_file_name))
                with open(output_path, 'w') as f:
                    c = csv.writer(f)
                    for i in range(6, 76):
                        c.writerow(sh_content[i])
            except KeyError:
                print('sheet not found in: {}'.format(file))
                pass
    print('Conversion complete!')
