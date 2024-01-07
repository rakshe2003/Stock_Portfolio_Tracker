import requests
import pandas as pd

class StockPortfolioTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def fetch_stock_price(self, symbol):
        base_url = 'https://www.alphavantage.co/query'
        function = 'GLOBAL_QUOTE'
        api_url = f'{base_url}?function={function}&symbol={symbol}&apikey={self.api_key}'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if 'Global Quote' in data:
                return float(data['Global Quote']['05. price'])
            else:
                print(f"Error fetching stock price for {symbol}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching stock price for {symbol}: {e}")
            return None

    def add_stock_to_portfolio(self, symbol, quantity):
        if symbol not in self.portfolio:
            self.portfolio[symbol] = 0
        self.portfolio[symbol] += quantity

    def display_portfolio_value(self):
        total_value = 0

        print("Stock Portfolio:")
        for symbol, quantity in self.portfolio.items():
            price = self.fetch_stock_price(symbol)
            if price is not None:
                value = price * quantity
                total_value += value
                print(f"{symbol}: {quantity} shares - Current Price: ${price:.2f} - Value: ${value:.2f}")

        print(f"Total Portfolio Value: ${total_value:.2f}")

# Example Usage
api_key = 'CXKA4S4LVJ313Z5F'
tracker = StockPortfolioTracker(api_key)

# Add stocks to the portfolio
tracker.add_stock_to_portfolio('AAPL', 10)
tracker.add_stock_to_portfolio('GOOGL', 5)

# Display the portfolio value
tracker.display_portfolio_value()
