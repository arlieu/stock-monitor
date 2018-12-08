import subprocess
import time
from utils.trade_scheduler import *


if __name__ == "__main__":
    while True:
        subprocess.run(["python", "stock_graphql_api/manage.py", "loaddata", "resources/output.json"])
        time.sleep(waitTime()/1000000)