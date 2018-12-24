# stock-monitor
Periodically scrapes NASDAQ for S&P 500 stock data and loads into a Django app. Data is made available via a GraphQL API/UI.

## Run Application
1. Download requirements: `pip install -r requirements.txt`.
2. Execute the run file: `python run.py` (may need to adjust `run.py` and `scheduled_task.py` to use a different python version/alias depending on your PATH variable).
3. Execute queries/mutations programmatically or on the UI.

**Instructions for using the UI**

4. Go to `<HOST>:8000/stocks` in browser.
5. Run GraphQL query or mutation in the input section (see example below). Documentation is generated in the right section of the UI.

**Query Example:**
```
query {
  stocks(search:"<SEARCH CRITERIA>"){
    symbol
    name
    bid
    ask
    target
    dayHigh
    dayLow
    shareVolume
    averageVolume
    previousClose
    yearHigh
    yearLow
    marketCap
    pe
    forwardPe
    eps
    dividend
    exDividendDate
    dividendDate
    currentYield
    beta
    openPrice
    closePrice
  }
}
```
* Note that all fields and the search filter are optional.

**Mutation Example:**
```
mutation {
  createStock(stockData: 
    {
      symbol:"<MANDATORY SYMBOL>", 
      name: "<MANDATORY NAME>",
      bid: "<OPTIONAL FIELD>",
      ask: "<OPTIONAL FIELD>",
      target: "<OPTIONAL FIELD>",
      dayHigh: "<OPTIONAL FIELD>",
      dayLow: "<OPTIONAL FIELD>",
      shareVolume: "<OPTIONAL FIELD>",
      averageVolume: "<OPTIONAL FIELD>",
      previousClose: "<OPTIONAL FIELD>",
      yearHigh: "<OPTIONAL FIELD>",
      yearLow: "<OPTIONAL FIELD>",
      marketCap: "<OPTIONAL FIELD>",
      pe: "<OPTIONAL FIELD>",
      forwardPe: "<OPTIONAL FIELD>",
      eps: "<OPTIONAL FIELD>",
      dividend: "<OPTIONAL FIELD>",
      exDividendDate: "<OPTIONAL FIELD>",
      dividendDate: "<OPTIONAL FIELD>",
      currentYield: "<OPTIONAL FIELD>",
      beta: "<OPTIONAL FIELD>",
      openPrice: "<OPTIONAL FIELD>",
      closePrice: "<OPTIONAL FIELD>"
    }
  ) {
    stock {
      name
      bid
      ask
      target
      dayHigh
      dayLow
      shareVolume
      averageVolume
      previousClose
      yearHigh
      yearLow
      marketCap
      pe
      forwardPe
      eps
      dividend
      exDividendDate
      dividendDate
      currentYield
      beta
      openPrice
      closePrice
    }
  }
}
```
* Note that only symbol and name fields are mandatory.

## Scraper
`StockCrawler` will take the file `input.txt`, which contains a list of S&P 500 companies by default, as input to determine the stock data to scrape. It spawns a child process for every process available to it and allocates each process a set number of stocks to handle. In the event that a server restricts the number of requests/blocks the IP being used, `StockCrawler` generates a list of 20 proxy IPs to use as alternates during every run. All processes will make a JSON dump to a common file `output.json`.

## Backend
Django app with a SQLite database. Only contains one model, `Stock`, which contains standard stock information presented on the NASDAQ site. Each stock in `output.json` is deserialized and updates the database.

## GraphQL API/UI
RPC API with a bootstraped UI implemented with the `graphene` library. Two request types: GET (filterable query) and POST (mutator).

## Scheduled Job
`StockCrawler` will run as a background process, scraping for the targeted companies every 30 minutes during NYSE 
trading hours (M-F: 9:30 AM - 4 PM EST). The deserialization and loading will occur for each scheduled run.

## To Do...
* Header spoofing to disguise requests*
* Multithread each process*
* Improve scheduled job timing

Additional tasks and problems can be found in the [Issues](https://github.com/arlieu/stock-monitor/issues) section.
