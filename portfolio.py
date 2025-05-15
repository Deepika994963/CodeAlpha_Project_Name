import os
import json
import yfinance as yf
import pandas as pd
from datetime import datetime

PORTFOLIO_FILE = 'portfolio.json'

# Utility functions for portfolio persistence
def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_portfolio(data):
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def add_stock(symbol, shares):
    portfolio = load_portfolio()
    symbol = symbol.upper()
    portfolio[symbol] = portfolio.get(symbol, 0) + shares
    save_portfolio(portfolio)
    print(f"Added {shares} shares of {symbol} to portfolio.")


def remove_stock(symbol):
    portfolio = load_portfolio()
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"Symbol {symbol} not found in portfolio.")



def fetch_portfolio():
    portfolio = load_portfolio()
    if not portfolio:
        print("Portfolio is empty.")
        return

    data = []
    total_value = 0.0
    for symbol, shares in portfolio.items():
        ticker = yf.Ticker(symbol)
        info = ticker.info
        current_price = info.get('regularMarketPrice') or ticker.history(period='1d')['Close'].iloc[-1]
        value = shares * current_price
        total_value += value
        data.append({
            'Symbol': symbol,
            'Shares': shares,
            'Price': current_price,
            'Value': value
        })

    df = pd.DataFrame(data)
    df['Value'] = df['Value'].map('${:,.2f}'.format)
    df['Price'] = df['Price'].map('${:,.2f}'.format)
    print(f"Portfolio as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(df.to_string(index=False))
    print(f"\nTotal Portfolio Value: ${total_value:,.2f}")



def menu():
    print("Stock Portfolio Tracker")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            sym = input("Enter ticker symbol: ")
            try:
                sh = float(input("Enter number of shares: "))
                add_stock(sym, sh)
            except ValueError:
                print("Invalid number of shares.")
        elif choice == '2':
            sym = input("Enter ticker symbol to remove: ")
            remove_stock(sym)
        elif choice == '3':
            fetch_portfolio()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()