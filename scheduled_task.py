import subprocess
import time

from crawler.trade_scheduler import *


if __name__ == "__main__":
    while True:
        nextRun = waitTime() / 1000000
        print("\nNEXT RUN: %d" % (nextRun))
        time.sleep(nextRun)
        subprocess.run(["python", "crawler/stock_crawler.py"])
        subprocess.run(["python", "stock_graphql_api/manage.py", "loaddata", "resources/output.json"])