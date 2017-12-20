#!/usr/bin/env bash

mongoimport -d ap_scores_db --collection scores --file ap_scores.json
mongoimport -d ap_scores_db --collection schools --file schools.json
mongoimport -d ap_scores_db --collection scores_female --file ap_scores_female.json
