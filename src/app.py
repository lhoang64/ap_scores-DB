#!/usr/bin/env python3

import web
from src.mongo_connection import MongoConnection

urls = ('/scores_by_state_all_demographics', 'get_scores_by_state_all',
        '/scores_by_state', 'get_scores_by_state',
        '/scores_by_year', 'get_scores_by_year',
        '/scores_by_year_and_state', 'get_scores_by_year_and_state',
        '/schools', 'schools_summary',
        '/', 'root'
        )

app = web.application(urls, globals())
conn = MongoConnection()
render_from_templates = web.template.render('templates')
render_from_static = web.template.render('static')

states_form = web.form.Form(web.form.Dropdown('states', [('Alabama', 'Alabama'), ('Alaska', 'Alaska'),
                                                ("Arizona", 'Arizona'), ("Arkansas", 'Arkansas'),
                                                ("California", 'California'), ("Colorado", 'Colorado'),
                                                ("Connecticut", 'Connecticut'), ("Delaware", 'Delaware'),
                                                ("DC", 'District Of Columbia'), ("Florida", 'Florida'),
                                                ("Georgia", 'Georgia'), ("Hawaii", 'Hawaii'), ("Idaho", 'Idaho'),
                                                ("Illinois", 'Illinois'), ("Indiana", 'Indiana'), ("Iowa", 'Iowa'),
                                                ("Kansas", 'Kansas'), ("Kentucky", 'Kentucky'),
                                                ("Louisiana", 'Louisiana'),
                                                ("Maine", 'Maine'),
                                                ("Maryland", 'Maryland'),
                                                ("Massachusetts", 'Massachusetts'),
                                                ("Michigan", 'Michigan'),
                                                ("Minnesota", 'Minnesota'),
                                                ("Mississippi", 'Mississippi'),
                                                ("Missouri", 'Missouri'),
                                                ("Montana", 'Montana'),
                                                ("Nebraska", 'Nebraska'),
                                                ("Nevada", 'Nevada'),
                                                ("New Hampshire", 'New Hampshire'),
                                                ("New Jersey", 'New Jersey'),
                                                ("New Mexico", 'New Mexico'),
                                                ("New York", 'New York'),
                                                ("North Carolina", 'North Carolina'),
                                                ("North Dakota", 'North Dakota'),
                                                ("Ohio", 'Ohio'),
                                                ("Oklahoma", 'Oklahoma'),
                                                ("Oregon", 'Oregon'),
                                                ("Pennsylvania", 'Pennsylvania'),
                                                ("Rhode Island", 'Rhode Island'),
                                                ("South Carolina", 'South Carolina'),
                                                ("South Dakota", 'South Dakota'),
                                                ("Tennessee", 'Tennessee'),
                                                ("Texas", 'Texas'),
                                                ("Utah", 'Utah'),
                                                ("Vermont", 'Vermont'),
                                                ("Virginia", 'Virginia'),
                                                ("Washington", 'Washington'),
                                                ("West Virginia", 'West Virginia'),
                                                ("Wisconsin", 'Wisconsin'),
                                                ("Wyoming", 'Wyoming')]),
                            web.form.Dropdown('scores', ['5', '4', '3', '2', '1']),
                            web.form.Dropdown('demographics', ['NOT STATED', 'ASIAN', 'BLACK', 'AMERICAN INDIAN',
                                                              'AMERICAN INDIAN/ALASKA NATIVE', 'HISPANIC/LATINO',
                                                              'MEXICAN AMERICAN', 'OTHER HISPANIC', 'PUERTO RICAN',
                                                              'WHITE', 'OTHER'])
                            )
year_form = web.form.Form(web.form.Dropdown('years', ['2017', '2016', '2015', '2014']),
                          web.form.Dropdown('scores', ['5', '4', '3', '2', '1']),
                          web.form.Dropdown('demographics', ['NOT STATED', 'ASIAN', 'BLACK', 'AMERICAN INDIAN',
                                                              'AMERICAN INDIAN/ALASKA NATIVE', 'HISPANIC/LATINO',
                                                              'MEXICAN AMERICAN', 'OTHER HISPANIC', 'PUERTO RICAN',
                                                              'WHITE', 'OTHER'])
                          )
year_state_form = web.form.Form(web.form.Dropdown('years', ['2017', '2016', '2015', '2014']),
                                web.form.Dropdown('states', [('Alabama', 'Alabama'), ('Alaska', 'Alaska'),
                                                             ("Arizona", 'Arizona'), ("Arkansas", 'Arkansas'),
                                                             ("California", 'California'), ("Colorado", 'Colorado'),
                                                             ("Connecticut", 'Connecticut'), ("Delaware", 'Delaware'),
                                                             ("DC", 'District Of Columbia'), ("Florida", 'Florida'),
                                                             ("Georgia", 'Georgia'), ("Hawaii", 'Hawaii'),
                                                             ("Idaho", 'Idaho'),
                                                             ("Illinois", 'Illinois'), ("Indiana", 'Indiana'),
                                                             ("Iowa", 'Iowa'),
                                                             ("Kansas", 'Kansas'), ("Kentucky", 'Kentucky'),
                                                             ("Louisiana", 'Louisiana'),
                                                             ("Maine", 'Maine'),
                                                             ("Maryland", 'Maryland'),
                                                             ("Massachusetts", 'Massachusetts'),
                                                             ("Michigan", 'Michigan'),
                                                             ("Minnesota", 'Minnesota'),
                                                             ("Mississippi", 'Mississippi'),
                                                             ("Missouri", 'Missouri'),
                                                             ("Montana", 'Montana'),
                                                             ("Nebraska", 'Nebraska'),
                                                             ("Nevada", 'Nevada'),
                                                             ("New Hampshire", 'New Hampshire'),
                                                             ("New Jersey", 'New Jersey'),
                                                             ("New Mexico", 'New Mexico'),
                                                             ("New York", 'New York'),
                                                             ("North Carolina", 'North Carolina'),
                                                             ("North Dakota", 'North Dakota'),
                                                             ("Ohio", 'Ohio'),
                                                             ("Oklahoma", 'Oklahoma'),
                                                             ("Oregon", 'Oregon'),
                                                             ("Pennsylvania", 'Pennsylvania'),
                                                             ("Rhode Island", 'Rhode Island'),
                                                             ("South Carolina", 'South Carolina'),
                                                             ("South Dakota", 'South Dakota'),
                                                             ("Tennessee", 'Tennessee'),
                                                             ("Texas", 'Texas'),
                                                             ("Utah", 'Utah'),
                                                             ("Vermont", 'Vermont'),
                                                             ("Virginia", 'Virginia'),
                                                             ("Washington", 'Washington'),
                                                             ("West Virginia", 'West Virginia'),
                                                             ("Wisconsin", 'Wisconsin'),
                                                             ("Wyoming", 'Wyoming')])
                                )
states_all_form = web.form.Form(web.form.Dropdown('states', [('Alabama', 'Alabama'), ('Alaska', 'Alaska'),
                                                ("Arizona", 'Arizona'), ("Arkansas", 'Arkansas'),
                                                ("California", 'California'), ("Colorado", 'Colorado'),
                                                ("Connecticut", 'Connecticut'), ("Delaware", 'Delaware'),
                                                ("DC", 'District Of Columbia'), ("Florida", 'Florida'),
                                                ("Georgia", 'Georgia'), ("Hawaii", 'Hawaii'), ("Idaho", 'Idaho'),
                                                ("Illinois", 'Illinois'), ("Indiana", 'Indiana'), ("Iowa", 'Iowa'),
                                                ("Kansas", 'Kansas'), ("Kentucky", 'Kentucky'),
                                                ("Louisiana", 'Louisiana'),
                                                ("Maine", 'Maine'),
                                                ("Maryland", 'Maryland'),
                                                ("Massachusetts", 'Massachusetts'),
                                                ("Michigan", 'Michigan'),
                                                ("Minnesota", 'Minnesota'),
                                                ("Mississippi", 'Mississippi'),
                                                ("Missouri", 'Missouri'),
                                                ("Montana", 'Montana'),
                                                ("Nebraska", 'Nebraska'),
                                                ("Nevada", 'Nevada'),
                                                ("New Hampshire", 'New Hampshire'),
                                                ("New Jersey", 'New Jersey'),
                                                ("New Mexico", 'New Mexico'),
                                                ("New York", 'New York'),
                                                ("North Carolina", 'North Carolina'),
                                                ("North Dakota", 'North Dakota'),
                                                ("Ohio", 'Ohio'),
                                                ("Oklahoma", 'Oklahoma'),
                                                ("Oregon", 'Oregon'),
                                                ("Pennsylvania", 'Pennsylvania'),
                                                ("Rhode Island", 'Rhode Island'),
                                                ("South Carolina", 'South Carolina'),
                                                ("South Dakota", 'South Dakota'),
                                                ("Tennessee", 'Tennessee'),
                                                ("Texas", 'Texas'),
                                                ("Utah", 'Utah'),
                                                ("Vermont", 'Vermont'),
                                                ("Virginia", 'Virginia'),
                                                ("Washington", 'Washington'),
                                                ("West Virginia", 'West Virginia'),
                                                ("Wisconsin", 'Wisconsin'),
                                                ("Wyoming", 'Wyoming')]),
                                web.form.Dropdown('scores', ['5', '4', '3', '2', '1'])
                                )
class root:
    def GET(self):
        return "TEST PAGE"

class schools_summary:
    def GET(self):
        record = conn.get_schools_collection()
        return render_from_templates.schools_summary(record)

class get_scores_by_state_all:
    def POST(self):
        form = states_all_form()
        form.validates()
        state = form.d.states
        score = form.d.scores
        demographics = ['NOT STATED', 'ASIAN', 'BLACK', 'AMERICAN INDIAN', 'AMERICAN INDIAN/ALASKA NATIVE',
                        'HISPANIC/LATINO', 'MEXICAN AMERICAN', 'OTHER HISPANIC', 'PUERTO RICAN', 'WHITE', 'OTHER']
        output = []
        for d in demographics:
            records = conn.get_records_by_state(state, score, d)
            output.append(records)
        return render_from_templates.all_by_state(output, state, score)

    def GET(self):
        form = states_all_form()
        return render_from_templates.search_by_state(form)

class get_scores_by_state:
    def POST(self):
        form = states_form()
        form.validates()
        state = form.d.states
        score = form.d.scores
        demographic = form.d.demographics
        records = conn.get_records_by_state(state, score, demographic)
        return render_from_templates.scores_by_state(records)

    def GET(self):
        form = states_form()
        return render_from_templates.search_by_state(form)

class get_scores_by_year:
    def POST(self):
        form = year_form()
        form.validates()
        year = form.d.years
        score = form.d.scores
        demographic = form.d.demographics
        records = conn.get_records_by_year(year, score, demographic)
        return render_from_templates.scores_by_year(records)

    def GET(self):
        form = year_form()
        return render_from_templates.search_by_year(form)

class get_scores_by_year_and_state:
    def POST(self):
        form = year_state_form()
        form.validates()
        year = form.d.years
        state = form.d.states
        record = conn.get_record_by_year_and_state(year, state)
        return render_from_templates.year_state_scores(record)

    def GET(self):
        form = year_state_form()
        return render_from_templates.search_year_state(form)

if __name__ == '__main__':
    app.run()
