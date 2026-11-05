import streamlit as st
import yfinance as yf
from datetime import date
 
st.title("Portfolio Analyzer")
 
# --- Input -------------------------------------------------------------
# TODO: allow more than one stock (ticker, purchase date, amount)
ticker = st.sidebar.text_input("Ticker", "ALV.DE")
buy_date = st.sidebar.date_input("Purchase date", date(2021, 9, 30))
benchmark = st.sidebar.selectbox("Benchmark", ["^GDAXI", "URTH", "^STOXX50E"])
 
 
# --- Data --------------------------------------------------------------
@st.cache_data
def load_prices(symbol, start):
    """Download adjusted closing prices (dividends included) from Yahoo Finance."""
    return yf.download(symbol, start=start, auto_adjust=True)["Close"].squeeze()
 
 
stock = load_prices(ticker, buy_date)
 
# --- Metrics -----------------------------------------------------------
# TODO: add the remaining metrics from case studies 2-4
total_return = stock.iloc[-1] / stock.iloc[0] - 1
st.metric("Total return", f"{total_return:.1%}")
 
# --- Charts ------------------------------------------------------------
st.line_chart({ticker: stock / stock.iloc[0] * 100})
 
# TODO: export results to Excel
 