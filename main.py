import streamlit as st
import yfinance as yf
import pandas as pd

# Function to get stock data
def get_stock_data(symbols, start_date, end_date):
    data = {}
    for symbol in symbols:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        data[symbol] = stock_data
    return data

# Streamlit app
st.title("Simple Stock Viewer")

# Multi-select box for choosing multiple stock symbols
selected_stocks = st.multiselect("Select stocks", ["AAPL", "GOOGL", "MSFT", "AMZN"])

# Date range selection
start_date = st.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-01-01"))

# Fetch stock data
if selected_stocks:
    stock_data = get_stock_data(selected_stocks, start_date, end_date)

    # Display stock data
    for symbol, data in stock_data.items():
        st.write(f"Stock Data for {symbol}")
        st.write(data.head())
else:
    st.warning("Please select at least one stock.")

# You can add more visualizations or analysis based on the stock data

