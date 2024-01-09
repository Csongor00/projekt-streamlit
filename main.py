import streamlit as st
import yfinance as yf  # Make sure to install yfinance using pip install yfinance

# Function to get stock data
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Streamlit app
st.title("Simple Stock Viewer")

# Select box for choosing a stock symbol
selected_stock = st.selectbox("Select a stock symbol", ["AAPL", "GOOGL", "MSFT", "AMZN"])

# Date range selection
start_date = st.date_input("Start Date", value="2022-01-01")
end_date = st.date_input("End Date", value="2023-01-01")

# Fetch stock data
stock_df = get_stock_data(selected_stock, start_date, end_date)

# Display stock data
st.write(f"Stock Data for {selected_stock}")
st.write(stock_df.head())

# You can add more visualizations or analysis based on the stock data

