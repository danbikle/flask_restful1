# demo14.py

# This script should demonstrate:
# flask_restful.Resource
# flask_restful.Api
# api.add_resource()
# URL-path-tokens
# sklearn LinearRegression

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo14.py
# curl localhost:5000/demo14/IBM/9/2017-12-31
import pdb
import os
import flask         as fl
import flask_restful as fr
import pandas        as pd
import numpy         as np
import datetime      as dt
import sklearn.linear_model as skl

application = fl.Flask(__name__)
api         = fr.Api(application)

class Demo14(fr.Resource):
  # I should tell get() about URL-path-tokens:
  def get(self, tkr='AAPL', yrs2train=8, date2predict='2018-01-01'):
    k1_s   = '1. You want to predict'
    k2_s   = '2. For this date'
    k3_s   = '3. By learning from this many years'
    k4_s   = '4. With '
    algo_s = 'Linear Regression'
    k5_s   = '5. And the prediction is '
    k6_s   = '6. Most recent price is '
    # I should get prices for tkr:
    prices0_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s='+tkr)
    # I should get most recent price:
    recent_price_f = prices0_df.Close[0]

    # See diagram: py4.us/cclasses/class04#r1
    prices1_df = prices0_df[['Date','Close']].sort_values(['Date'])
    # I should get training data.
    max_date_s  = prices1_df['Date'].max()
    max_date_dt = dt.datetime.strptime(max_date_s, '%Y-%m-%d')
    # I should get min-date in the training data.
    min_date_dt = max_date_dt - dt.timedelta(days=(yrs2train * 365))
    min_date_s  = dt.datetime.strftime(min_date_dt, '%Y-%m-%d')
    # I should get training data.

    # See diagram: py4.us/cclasses/class04#r1
    prices2_df = prices1_df.copy()[prices1_df.Date >= min_date_s]
    # I should convert Date from string to datetime:
    prices2_df['cdate'] = pd.to_datetime(prices2_df.Date)
    # I should convert cdate to integer
    days_delt_sr = prices2_df.cdate - min_date_dt
    days_i_sr    = (days_delt_sr / np.timedelta64(1, 'D')).astype(int)

    # See diagram: py4.us/cclasses/class04#r1
    prices2_df['days'] = days_i_sr
    # I should fit a linear model:
    linr_model     = skl.LinearRegression()
    x_wrongshape_a = np.array(prices2_df.days)

    # See diagram: py4.us/cclasses/class04#r1
    x_a = np.reshape(x_wrongshape_a, (len(x_wrongshape_a),1))
    y_a = np.array(prices2_df.Close)

    # See diagram: py4.us/cclasses/class04#r1
    linr_model.fit(x_a,y_a)
    # I should convert date2predict to integer of days past min_date_dt
    date2predict_dt = dt.datetime.strptime(date2predict, '%Y-%m-%d')
    date2predict_i  = (date2predict_dt - min_date_dt).days

    # See diagram: py4.us/cclasses/class04#r1
    prediction_f    = linr_model.predict(date2predict_i)[0]
    return {k1_s:tkr
            ,k2_s:date2predict
            ,k3_s:yrs2train
            ,k4_s:algo_s
            ,k5_s:prediction_f
            ,k6_s:recent_price_f
    }
# I should declare URL-path-tokens, and I should constrain them:
api.add_resource(Demo14, '/demo14/<tkr>/<int:yrs2train>/<date2predict>')
# curl localhost:5000/demo14/IBM/9/2017-12-31

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
