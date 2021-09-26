from flask import Blueprint,render_template,request,flash,jsonify
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,LSTM
import investpy as inv
import os
import json
import plotly
import plotly.express as px

invests = Blueprint('invests', __name__)

@invests.route('/invests',methods=['GET'])
#@login_required
# def invest():#this functon name cannot same as blueprint name
# #load data
#   company = 'FB'
#   start =dt.datetime(2012,1,1)
#   end =dt.datetime(2021,9,1)
#   data = web.DataReader(company,'yahoo',start,end)
# #prepare data
#   scaler = MinMaxScaler(feature_range=(0,1))
#   scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

#   prediction_days =60
#   x_train =[]
#   y_train =[]

#   for x in range(prediction_days, len(scaled_data)):
#     x_train.append(scaled_data[x-prediction_days:x,0])
#     y_train.append(scaled_data[x,0])
#   x_train,y_train =np.array(x_train),np.array(y_train)
#   x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
# #build the model
#   model = Sequential()

#   model.add(LSTM(units=50,return_sequences=True, input_snape=(x_train.shape[1],1)))
#   model.add(Dropout(0,2))

#   model.add(LSTM(units=50,return_sequences=True))
#   model.add(Dropout(0,2))
#   model.add(LSTM(units=50))
#   model.add(Dropout(0,2))
#   model.add(Dense(units=1))# 'Predicton of the next clost'

#   model.compile(optimizer='adam',loss='mean_squared_error')
#   model.fit(x_train,y_train,opochs=25,batch_size=32)

# #test model
# #load test dat
#   test_start =dt.datetime(2021,1,1)
#   test_end =dt.datetime.now()
#   test_data = web.DataReader(company,'yahoo',test_start,test_end)
#   actual_prices = test_data['Close'].values
#   total_dataset = pd.concat((data['Close'],test_data['Close']),axis=0)

#   model_inputs = total_dataset[len(total_dataset)-len(test_data)- prediction_days:].values
#   model_inputs = model_inputs.reshape(-1,1)
#   model_inputs = scaler.transform(model_inputs)

# #make predictions on test data

#   x_test=[]
#   for x in range(prediction_days, len(model_inputs)):
#     x_test.append(model_inputs[x-prediction_days:x,0])

#   x_test =np.array(x_train)
#   x_test = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

#   predicted_prices = model.predict(x_test)
#   predicted_prices = scaler.inverse_transform(predicted_prices)
# #plot the test
#   plt.plot(actual_prices, color="black",label=f"Actual {company} Price")
#   plt.plot(predicted_prices, color="green",label=f"Predict {company} Price")
#   plt.title(f"{company} Share Price")
#   plt.xlabel('Time')
#   plt.ylabel(f"{company} Share Price")
#   plt.legend()
#   plt.show()
#   return render_template("home.html",test="tst")
@invests.route('/invest')
#@login_required
def investsimple():
  #stocks = ["WEGE3", "JHSF3"]
  stocks = ["TRP"]
  dfs = list()
  #test_start =dt.strptime('21/6/2021', '%d/%m/%Y')
  test_start ='01/01/2020'
  test_end ='01/01/2021'
 
  for stock in stocks:
    datainitial = inv.get_stock_historical_data(stock=stock,
                                        country='Canada',
                                        from_date=test_start,
                                        to_date=test_end)
    df = datainitial["Open"]
    #dte =datainitial["Date"]
    dfclose = datainitial["Close"]
    dflow = datainitial["Low"]
    dfhigh = datainitial["High"]
    dfs.append(df)
    #dfs.append([{'Open':df,'Close':dfclose,'Low':dflow,'High':dfhigh}])
    i=len(df)
    df1 = pd.DataFrame(dict(
      Date = range(i),
      Price = df
    ))
    Close=dfclose
    fig1 = px.line(df1, x="Date", y="Price", title='Stock Canada')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    
    #fig1.add_scatter(x=['Date'], y=['Close'], mode='lines')




  return render_template("invest.html",user ='user',datesimple=dfs,graph1JSON=graph1JSON )

