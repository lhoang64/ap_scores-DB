#!/usr/bin/env python3

from pymongo import MongoClient

class MongoConnection:
    def __init__(self):
        self.client = MongoClient()
        self.database = self.client.ap_scores_db

    def get_records_by_state(self, state, score, demographic):
        collection = self.database.scores
        records = collection.find({'state': state}, {'scores.{0}.{1}'.format(score, demographic): '1', 'state':  '1'})
        total_in_state = collection.find({'state': state}, {'scores.{0}.{1} TOTAL'.format(score, state.upper()): '1'})
        output = {'State': state, 'Demographic': demographic, 'Score': score, 'Total number students': 0,
                  'Total number of students in state': 0}
        for r in records:
            for dictionary in r['scores'][score]:
                if dictionary:
                    if dictionary[demographic] not in ['*', 'NoData', '']:
                        output['Total number students'] += int(dictionary[demographic])
                    else:
                        output['Total number students'] += 0
        for r in total_in_state:
            for dictionary in r['scores'][score]:
                if dictionary:
                    if dictionary['{0} TOTAL'.format(state.upper())] not in ['*', 'NoData', '']:
                        output['Total number of students in state'] += int(dictionary['{0} TOTAL'.format(state.upper())])
                    else:
                        output['Total number of students in state'] += 0
        return output

    def get_records_by_year(self, year, score, demographic):
        collection = self.database.scores
        records = collection.find({'year': year}, {'scores.{0}.{1}'.format(score, demographic): '1', 'year': '1'})
        output = {'Year': year, 'Demographic': demographic, 'Score': score, 'Total number students': 0}
        for r in records:
            for dictionary in r['scores'][score]:
                if dictionary:
                    if dictionary[demographic] not in ['*', 'NoData', '']:
                        output['Total number students'] += int(dictionary[demographic])
                    else:
                        output['Total number students'] += 0
        return output

    def get_record_by_year_and_state(self, year, state):
        collection = self.database.scores
        records = collection.find({'year': year, 'state': state}, {'_id': 0, 'scores': '1'})
        output = {'1': '', '2': '', '3': '', '4': '', '5': ''}
        for r in records:
            for key in output:
                output[key] = r['scores'][key]
        return output

    def get_schools_collection(self):
        collection = self.database.schools
        record = collection.find_one({}, {'_id': 0})
        return record

    def get_records_by_year_female(self, year, score, demographic):
        collection = self.database.scores_female
        records = collection.find({'year': year}, {'scores.{0}.{1}'.format(score, demographic): '1', 'year': '1'})
        output = {'Year': year, 'Demographic': demographic, 'Score': score, 'Total number students': 0}
        for r in records:
            for dictionary in r['scores'][score]:
                if dictionary:
                    if dictionary[demographic] not in ['*', 'NoData', '']:
                        output['Total number students'] += int(dictionary[demographic])
                    else:
                        output['Total number students'] += 0
        return output

