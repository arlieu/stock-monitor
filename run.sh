#!/usr/bin/env bash

printf "%s\nMaking migrations...\n\n" "----------------------------------------"

echo python stock_graphql_api/manage.py makemigrations
echo python stock_graphql_api/manage.py migrate

printf "%s\nCreating repeated tasks...\n\n" "----------------------------------------"

echo schtasks //create //tn scrape-and-load //tr '"python /crawler/stock_crawler.py && python stock_graphql_api/manage.py loaddata /resources/output.json"' //sc daily //st 09:30 //ri 60 //et 16:00

printf "%s\nRunning stock-monitor...\n\n" "----------------------------------------"

echo python stock_graphql_api/manage.py runserver --noreload

printf "%s\nTERMINATED\n\n" "--------------------------------"