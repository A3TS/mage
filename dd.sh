i#!/bin/bash

# API endpoint URL
API_URL="http://34.117.217.236/devops-interview/v1/pipeline"
AUTH_TOKEN="xxxxxxxx"


# Fetch the data and save it as pipeline_data.json
curl --header "Authorization: Bearer $AUTH_TOKEN" -v "$API_URL" | jq . > pipeline_data.json

# Extract and aggregate the pipeline data using jq and save it as pipeline_job_summary.csv
jq -r '.payload[] | select(.status_reason != "think_it_passed") | [.status, .status_reason] | @csv' pipeline_data.json |
awk -F',' '{ reasons[$1","$2]++ } END { for (reason in reasons) print reason","reasons[reason] }' |
sort > pipeline_job_summary.csv
echo "Status,Reason,Occurrences" | cat - pipeline_job_summary.csv > temp && mv temp pipeline_job_summary.csv
