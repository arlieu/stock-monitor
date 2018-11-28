#!/usr/bin/env bash

echo schtasks /run /tn "python stock_graphql_api/manage.py makemigrations &&
    python stock_graphql_api/manage.py migrate && python stock_graphql_api/manage.py runserver"

echo schtasks /create
    /tn scrape-and-load
    /tr "python /crawler/stock_crawler.py && python stock_graphql_api/manage.py loaddata ../resources/output.json"
    /sc daily
    /st 09:30 /ri 30 /et16:00

$SHELL