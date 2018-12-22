# stock-monitor
Periodically scrapes NASDAQ for stock data and loads into a Django app. Data is made available via a GraphQL API/UI.

### Run Application
1. Download requirements: `pip install -r requirements.txt`
2. Execute the run file: `python run.py` (may need to adjust `run.py` and `scheduled_task.py` to use a different python version/alias depending on your PATH variable).
