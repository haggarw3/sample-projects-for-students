StockMarketProj

This project is a webpage that presents information for 100 stocks in the S&P 500. The python script connects to AlphaVantage's API (API documentation: https://www.alphavantage.co/documentation/). The API's response includes the stocks' opening price, closing price, high price, low price, and trade volume for the current day. The top 5 stocks with the largest gains and the top 5 stocks with the least gains are also calculated for later presentation in the front-end. 

Instructions:

1. 'app_final.py' must be run first to request data from stock market API. All stock data is written to 'stock_data.json'.

2.'create_xml.py' must be run after  'app_final.py' to dump data from 'stock_data.json' to 'stock_data.xml' for front-end use. 

3. display XML in browser. Easiest way is to run the stock_data.xml file from an IDE such as Pycharm, VisualStudio, or Netbeans. 