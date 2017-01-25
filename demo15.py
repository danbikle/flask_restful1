# demo15.py

# This script should demonstrate:
# flask_restful.Resource
# flask_restful.Api
# api.add_resource()
# URL-path-tokens
# sklearn LinearRegression

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo15.py
# curl localhost:5000/demo15/IBM/9/2017-12-31
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

class Demo15(fr.Resource):
  # I should tell get() about URL-path-tokens:
  def get(self, tkr='AAPL', yrs2train=8, date2predict='2018-01-01'):
    k1_s   = '1. You want to predict'
    k2_s   = '2. For this date'
    k3_s   = '3. By learning from this many years'
    k4_s   = '4. With '
    algo_s = 'Logistic Regression'
    k5_s   = '5. And the prediction is '
    k6_s   = '6. Most recent price is '
    return {'under': 'construction'}
# I should declare URL-path-tokens, and I should constrain them:
api.add_resource(Demo15, '/demo15/<tkr>/<int:yrs2train>')
# curl localhost:5000/demo15/IBM/9

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'

