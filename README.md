## Computer Science A AP score distribution

College Board publicizes its data on the score distributions for differnet demographics. The original data contained information on all available AP subject exams, however for this project I focused on the CS A exams to look at the data there. The original format of the data was .xlsx files, seperated by state and year. The goal of this project was to aggregate and convert the data from the .xlsx files into one Mongo database.

### Building the Mongo database
All files needed to build the database is located in the data folder. The data is in schools.json, ap_scores.json, ap_scores_female.json, and ap_scores_male.json. Running the setup_db.sh script will run the imports to set up the database.

### DB 'schema'
There are four collections in the database:
* schools - contains data on the number of schools that offer CS A AP exams from 2008-2017
* scores - contains data on the score distribution by race
* scores_female - contains data on the score distribution by race for those who identified as female
* scores_male - contains data on the score distribution by race for those who identified as male

Sample record in scores collection:
```
{ 	
“year”: 2008,
“state”: “AL”, 
“scores”: { "5" : { “asian”: "10"},
				  “black”: "10"},
		           …
		        },
	    	"4" : { … },
	     	 …
		  }
}

```

### Web.py app
The web.py app lets you query the database for score distribution for state or by year. Currently it is only connected to the scores collections, so queries for the scores_female and scores_male collections are not available.
To run the app, simply run the app.py file in the src directory.
