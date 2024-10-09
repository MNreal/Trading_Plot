# Data Analysis Tools
import numpy as np
import pandas as pd

# Import datetime module
import datetime as dt

# Fetch stock data from Yahoo Finance
import yfinance as yf

# Plotting tools
import matplotlib.pyplot as plt

# --- Date Handling ---

# Get current date
current_date = dt.datetime.now()
sorted_date = current_date.strftime('%Y-%m-%d')

# Get date for the next day (+1)
one_day = current_date + dt.timedelta(days=1)
sorted_one_day = one_day.strftime('%Y-%m-%d')

# Get date for 5 days ago (-5)
five_date = current_date - dt.timedelta(days=5)
sorted_five_date = five_date.strftime('%Y-%m-%d')

# Get date for yesterday (-1)
yesterday_date = current_date - dt.timedelta(days=1)
sorted_yesterday_date = yesterday_date.strftime('%Y-%m-%d')

# --- Fetch Forex Data ---

# Get forex data from yesterday to the current date (daily interval)
forex_data_days = yf.download('EURUSD=X', start=sorted_yesterday_date, end=sorted_one_day, interval='1d')
forex_data_days.index = pd.to_datetime(forex_data_days.index)

# Display fetched data (daily)
print(forex_data_days)

# Get forex data for the last day (minute interval)
forex_data_minute = yf.download('EURUSD=X', start=sorted_yesterday_date, end=sorted_one_day, interval='1m')
forex_data_minute.index = pd.to_datetime(forex_data_minute.index)

# Transform datetime to string for easier plotting
forex_data_minute['dates'] = forex_data_minute.index.strftime('%Y-%m-%d %H:%M:%S')

# Fetch Weekly Data
weekly_data = yf.download('EURUSD=X', start=sorted_five_date, end=sorted_one_day, interval='1wk')
weekly_data.index = pd.to_datetime(weekly_data.index)

# --- Plotting Forex Data ---

# Create plot with a larger figure size
fig, ax = plt.subplots(figsize=(15, 7))

# Plot 'Adj Close' prices against time (minute data)
ax.plot(forex_data_minute['dates'], forex_data_minute['Adj Close'], label='Minute Data', color='blue')

# Set axis titles and labels
plt.title('EUR/USD Exchange Rate (Minute & Weekly Data)', fontsize=16)
plt.xlabel('Time', fontsize=16)
plt.ylabel('Price (Adjusted Close)', fontsize=16)

# Set ticks size and rotation
plt.xticks(fontsize=6, rotation=60)
plt.yticks(fontsize=6)

# Add a legend
plt.legend(prop={'size': 14})

# Max tick locators to avoid overcrowding
ax.xaxis.set_major_locator(plt.MaxNLocator(80))

# Display the plot
plt.show()

# --- Price Movement Analysis ---

# Convert 'Adj Close' prices to a list
forex_data_list = forex_data_minute['Adj Close'].tolist()

# Initial price
initial_price = forex_data_list[0]
print(forex_data_list)

# Initialize buy/sell counter
buy_counter = 0

# Loop through the price list and compare consecutive prices
for i in range(len(forex_data_list) - 1):
    price_current = forex_data_list[i]
    price_next = forex_data_list[i + 1]
    
    print("Current Price:", price_current)
    print("Next Price:", price_next)

    # Determine whether to buy or sell based on price movement
    if (price_next - price_current) < 0:
        buy_counter -= 1
    elif (price_next - price_current) > 0:
        buy_counter += 1

# Output the result of buy/sell decision
if buy_counter < 0:
    print("Sell")
    print("Buy Counter:", buy_counter)
elif buy_counter > 0:
    print("Buy")
    print("Buy Counter:", buy_counter)
else:
    print("Do Nothing")
    print("Buy Counter:", buy_counter)
