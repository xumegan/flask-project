# import streamlit as st
# import yfinance as yf
# # import matplotlib.pyplot as plt
# # import pandas as pd
# # import pandas_datareader as web
# import datetime as dt
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# from plotly import graph_objs as go

# #load data
# company = 'FB'
# START ="2015-01-01" #dt.datetime(2012,1,1)
# TODAY =date.today().strftime("%Y-%m-%d")

# st.title("stock prediction app")
# stocks =("AAPL","GOOG","MSFT","GME")
# selected_stocks = st.selectbox("Select dataset for prediction", stocks)
# n_year = st.slider("years of predition",1,4)
# period = n_years = 365

# def load_data(ticker):
#   data = yf.download(ticker,START,TODAY)
#   data.reset_index(inplace=True)
#   return data

# data_load_state = st.text("Load data..")
# data = load_data(selected_stocks)
# data_load_state.text("Load data... done!")

# st.subheader('Raw data')
# st.write(data.tail())

# def plot_raw_data():
#   fig = go.Figure()
#   fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
#   fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_close'))
#   fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True)
#   st.plotly_chart(fig)
# plot_raw_data()
