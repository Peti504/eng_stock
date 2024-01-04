import yfinance as yf
import streamlit as st

st.write("""
# Szimpla részvényárfolyam megjelnítése streamlit segítségével

A részvények záró és készletvolumenének árát mutatja a google szerint!

""")


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')



st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)  