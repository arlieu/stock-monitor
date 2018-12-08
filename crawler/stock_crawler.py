from lxml import html
import requests
import json
from enum import Enum
import datetime
from django.core.serializers.json import DjangoJSONEncoder


class DataType(Enum):
    TEXT = 1
    DECIMAL = 2
    BIGINTEGER = 3
    DATE = 4


class StockCrawler:
    def __init__(self):
        self.stocksList = []
        self.url = "http://www.nasdaq.com/symbol/"
        self.urlSet = set()
        for line in open("resources/input.txt"):
            line = line.strip()
            ticker = line.split(',')[0]
            self.urlSet.add(self.url + ticker)

        self.keyTransformations = {
            "Best Bid / Ask": "bid/ask",
            "1 Year Target": "target",
            "Today's High / Low": "day_high/day_low",
            "Share Volume": "share_volume",
            "50 Day Avg. Daily Volume": "average_volume",
            "90 Day Avg. Daily Volume": "average_volume",
            "Previous Close": "previous_close",
            "52 Week High / Low": "year_high/year_low",
            "Market Cap": "market_cap",
            "P/E Ratio": "pe",
            "Forward P/E (1y)": "forward_pe",
            "Earnings Per Share (EPS)": "eps",
            "Annualized Dividend": "dividend",
            "Ex Dividend Date": "ex_dividend_date",
            "Dividend Payment Date": "dividend_date",
            "Current Yield": "current_yield",
            "Beta": "beta",
        }

        self.valueTransformations = {
            "open_price": DataType.DECIMAL,
            "close_price": DataType.DECIMAL,
            "bid": DataType.DECIMAL,
            "ask": DataType.DECIMAL,
            "target": DataType.DECIMAL,
            "day_high": DataType.DECIMAL,
            "day_low": DataType.DECIMAL,
            "share_volume": DataType.BIGINTEGER,
            "average_volume": DataType.BIGINTEGER,
            "previous_close": DataType.DECIMAL,
            "year_high": DataType.DECIMAL,
            "year_low": DataType.DECIMAL,
            "market_cap": DataType.BIGINTEGER,
            "pe": DataType.DECIMAL,
            "forward_pe": DataType.DECIMAL,
            "eps": DataType.DECIMAL,
            "dividend": DataType.DECIMAL,
            "ex_dividend_date": DataType.DATE,
            "dividend_date": DataType.DATE,
            "current_yield": DataType.DECIMAL,
            "beta": DataType.DECIMAL,
        }

        self.model = "stocks.Stock"
        count = 1

        print("Scanning the S&P 500\n")
        for url in self.urlSet:
            symbol = url.split('/')[-1]
            print("Processing " + symbol + " (" + str(count) + "/505)" + "...", end=" ")
            stockDictionary = {}
            stockDictionary["pk"] = symbol
            stockDictionary["model"] = self.model
            stockDictionary["fields"] = self.parse(self.openSite(url).text)
            stockDictionary["fields"]["symbol"] = symbol
            self.stocksList.append(stockDictionary)
            count += 1
            print("Done!")
            if count > 10:
                break

        print("------------------------------------------\nAll stocks loaded!\n")
        # currentDateTime = datetime.datetime.now()
        # with open("resources/output-%d-%d-%d_%d-%d-%d.json" %
        #           (currentDateTime.year,
        #            currentDateTime.month,
        #            currentDateTime.day,
        #            currentDateTime.hour,
        #            currentDateTime.minute,
        #            currentDateTime.microsecond),
        #           'w') as fp:
        #     json.dump(self.stocksList, fp, indent=4, ensure_ascii=False, cls=DjangoJSONEncoder)
        # print("View 'resources/output-%s.json' for results" % currentDateTime)
        with open("resources/output.json", 'w') as fp:
            json.dump(self.stocksList, fp, indent=4, ensure_ascii=False, cls=DjangoJSONEncoder)
        print("View 'resources/output.json' for results")

    def openSite(self, url):
        try:
            return requests.get(url)
        except requests.exceptions.HTTPError as eh:
            print("Http Error:", eh)
        except requests.exceptions.ConnectionError as ec:
            print("Error Connecting:", ec)
        except requests.exceptions.Timeout as et:
            print("Timeout Error:", et)
        except requests.exceptions.RequestException as e:
            print("Server Error:", e)

    def transformKey(self, key):
        return self.keyTransformations.get(key)

    def transformValue(self, key, value):
        transform = self.valueTransformations[key]
        if transform == DataType.TEXT:
            return value
        elif transform == DataType.DECIMAL:
            return float(value)
        elif transform == DataType.BIGINTEGER:
            return int(value)
        elif transform == DataType.DATE:
            dateParts = list(map(int, value.split('/')))
            return datetime.date(dateParts[2], dateParts[0], dateParts[1])
        else:
            return None

    def parse(self, data):
        parser = html.fromstring(data)

        xpath_head = "//div[@id='qwidget_pageheader']//h1//text()"
        xpath_key_stock_table = '//div[@class="row overview-results relativeP"]//div[contains(@class,' \
                                '"table-table")]/div'
        xpath_open_price = '//b[contains(text(),"Open Price:")]/following-sibling::span/text()'
        xpath_close_price = '//b[contains(text(),"Close Price:")]/following-sibling::span/text()'
        xpath_key = './/div[@class="table-cell"]/b/text()'
        xpath_value = './/div[@class="table-cell"]/text()'

        raw_name = parser.xpath(xpath_head)
        key_stock_table = parser.xpath(xpath_key_stock_table)
        raw_open_price = parser.xpath(xpath_open_price)
        raw_close_price = parser.xpath(xpath_close_price)

        company_name = raw_name[0].split("Common")[0].split("(")[0].strip() if raw_name else ''
        open_price = raw_open_price[0].replace(" ", "").replace(",", "").replace("$", "")\
            .strip() if raw_open_price else None
        close_price = raw_close_price[0].replace(" ", "").replace(",", "").replace("$", "")\
            .strip() if raw_close_price else None

        nasdaq_data = {
            "name": company_name,
            "open_price": float(open_price) if open_price is not None else None,
            "close_price": float(close_price) if open_price is not None else None,
        }

        for i in key_stock_table:
            key = i.xpath(xpath_key)
            value = i.xpath(xpath_value)
            key = ''.join(key).strip()
            key1, key2 = "", ""
            value1, value2 = None, None
            slashCount = key.count('/')
            value = ' '.join(''.join(value).split()).replace(",", "").replace("$", "").replace("%", "")

            if slashCount == 1 and "P/E" not in key:
                if "Best" in key:
                    key1 = "bid"
                    key2 = "ask"
                elif "Today" in key:
                    key1 = "day_high"
                    key2 = "day_low"
                elif "52" in key:
                    key1 = "year_high"
                    key2 = "year_low"

                value1 = value.split('/')[0].strip()
                value2 = value.split('/')[1].strip()

            if value1 is None:
                trueKey = self.transformKey(key)
                if trueKey is not None:
                    try:
                        nasdaq_data[trueKey] = self.transformValue(trueKey, value)
                    except Exception as e:
                        nasdaq_data[trueKey] = None
            else:
                if key1 is not None:
                    try:
                        nasdaq_data[key1] = self.transformValue(key1, value1)
                    except Exception as e1:
                        nasdaq_data[key1] = None
                if key2 is not None:
                    try:
                        nasdaq_data[key2] = self.transformValue(key2, value2)
                    except Exception as e2:
                        nasdaq_data[key2] = None

        return nasdaq_data


if __name__ == "__main__":
    StockCrawler()