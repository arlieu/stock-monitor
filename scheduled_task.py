import subprocess
import time

from crawler.stock_crawler import StockCrawler
from utils.trade_scheduler import *


if __name__ == "__main__":
    stockCrawler = StockCrawler()
    while True:
        stockCrawler.execute()
        subprocess.run(["python", "stock_graphql_api/manage.py", "loaddata", "resources/output.json"])
        nextRun = waitTime() / 1000000
        print("\nNEXT RUN in %ds" % (nextRun))
        time.sleep(nextRun)