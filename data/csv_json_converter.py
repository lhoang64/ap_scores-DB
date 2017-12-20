#!/usr/bin/env python3

"""
    desc: Class used to convert csv files generated in excel_csv_converter to json files to be used in Mongodb
    author: Linh Hoang <lhoang@bennington.edu>
    date: 12/5/17
"""

import csv


class Record:
    def __init__(self, year, subject, path_to_csv):
        self.year = year
        self.subject = subject
        self.path_to_csv = path_to_csv
        self.record = {'year': self.year, 'scores': {'5': None, '4': None, '3': None, '2': None,
                                                     '1': None}}

    def to_dict(self):
        return self.record

    def set_scores(self):
        for key in self.record['scores']:
            self.record['scores'][key] = self._get_record_for_score(key)

    def _get_record_for_score(self, score):
        record = []
        with open(self.path_to_csv, 'r') as f:
            c = csv.reader(f)
            for r in c:
                if r[2] == score:
                    race = r[1].strip()
                    num_students_csa = r[10].replace(' ', '')
                    students = {race: num_students_csa}
                    record.append(students)
        return record


