import yfinance as yf
import streamlit as st 
import pandas as pd


ticker_symbol   = "AAPL"

st.write("""
Apple
""")



ticker_data     = yf.Ticker(ticker_symbol) 

ticker_df = ticker_data.history(period="1d", start='2019-02-02', end='2022-1-1')

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)