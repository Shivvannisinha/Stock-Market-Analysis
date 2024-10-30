import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate sample stock data
def generate_sample_stock_data():
    dates = pd.date_range(start='2020-01-01', end='2023-01-01', freq='B')  # Business days
    prices = np.random.normal(loc=100, scale=10, size=len(dates)).cumsum()  # Simulated stock prices
    adj_close = prices + np.random.normal(loc=0, scale=1, size=len(dates))  # Adjusted close prices
    stock_data = pd.DataFrame(data={'Adj Close': adj_close}, index=dates)
    return stock_data

# Function to calculate daily returns and moving averages
def analyze_stock_data(stock_data):
    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
    stock_data['SMA 50'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['SMA 200'] = stock_data['Adj Close'].rolling(window=200).mean()
    return stock_data

# Function to visualize stock price and moving averages
def visualize_stock_data(stock_data, ticker):
    plt.figure(figsize=(14, 7))
    plt.title(f"{ticker} Stock Price and Moving Averages")
    plt.plot(stock_data['Adj Close'], label='Adjusted Close', color='blue')
    plt.plot(stock_data['SMA 50'], label='50-Day SMA', color='orange')
    plt.plot(stock_data['SMA 200'], label='200-Day SMA', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    ticker = 'Sample Stock'  # Example ticker

    # Generate sample stock data
    stock_data = generate_sample_stock_data()
    analyzed_data = analyze_stock_data(stock_data)
    visualize_stock_data(analyzed_data, ticker)
