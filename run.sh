#!/usr/bin/env bash

printf "%s\nMaking migrations...\n\n" "----------------------------------------"

echo python stock_graphql_api/manage.py makemigrations &&
    python stock_graphql_api/manage.py migrate

printf "\n%s\nCreating scheduled tasks...\n\n" "----------------------------------------"

echo schtasks //create //tn scrape-and-load //tr '"python /crawler/stock_crawler.py && python stock_graphql_api/manage.py loaddata /resources/output.json"' //sc daily //st 09:30 //ri 60 //et 16:00

printf "\n%s\nRunning stock-monitor...\n\n" "----------------------------------------"

echo python stock_graphql_api/manage.py runserver

printf "\nTERMINATED\n%s\n" "----------------------------------------"

$SHELL