from flask import Blueprint,render_template,request,flash,jsonify
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import investpy as inv
import json
import plotly
import plotly.express as px

invests = Blueprint('invests', __name__)

@invests.route('/invest', methods=['POST'])
def form_post():
  if request.method == 'POST':
    startdate = request.form.get('startdate')
    enddate = request.form.get('enddate')
    pickstock = request.form.get('pickstock')
    user =''
    if user:
        flash('logined',category='success')        
    else:    
      flash('email not exist',category='error')
  return render_template("invest.html",user ='user')

@invests.route('/invest')
#@login_required
def investsimple():
  #stocks = ["WEGE3", "JHSF3"]
  stocks = ["TRP"]
  dfs = list()
  test_start ='20/07/2021'
  test_end ='24/09/2021'
 
  for stock in stocks:
    datainitial = inv.get_stock_historical_data(stock=stock,
                                        country='Canada',
                                        from_date=test_start,
                                        to_date=test_end,
                                        as_json=False,
                                        order='ascending', interval='Daily')
    dates=datainitial.index
    dfopen = datainitial["Open"]
    dfclose = datainitial["Close"]
    dfs.append({'date':dates.strftime('%-m/%-d/%Y'),'open':dfopen,'close':dfclose})
    k=len(dfopen)
    
    df1 = pd.DataFrame(dict( Date = dates,Price = dfopen))
    fig = px.line(df1, x="Date", y="Price", title=stock+' '+'Stock Canada')
    
    df2 = pd.DataFrame(dict( Date = dates,Close = dfclose))
    fig.add_scatter(x=df2['Date'], y=df2['Close'], mode='lines')
    
    fig.update_xaxes(
      rangeslider_visible=True,
      rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
      )
    )

    graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
 
  return render_template("invest.html",user ='user',datesimple=dfs,graph1JSON=graph1JSON, k=k,stocks=stocks)

#datainitial = inv.get_stock_historical_data(stock=stock,
 #                                       country='Canada',
  #                                      from_date=test_start,
  #                                      to_date=test_end,
  #                                      as_json=False,#output data format, either a pandas.DataFrame or json. {name: name,historical: [{date: 'dd/mm/yyyy',open: x,high: x,low: x,close: x,volume: x,currency: x},...]}
  #                                      order='ascending', interval='Daily'),# value to define the historical data interval to retrieve, by default Daily, but it can also be Weekly or Monthly.
   