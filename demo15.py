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
# curl localhost:5000/demo15/IBM/2016/9
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
  def get(self, tkr='AAPL', yr2predict='2017', yrs2train=8):
    k1_s   = '1. You want to predict'
    k2_s   = '2. For this year'
    k3_s   = '3. By learning from this many years'
    k4_s   = '4. With '
    algo_s = 'Linear Regression'
    return {k1_s:tkr
            ,k2_s:yr2predict
            ,k3_s:yrs2train
            ,k4_s:algo_s
    }
# I should declare URL-path-tokens, and I should constrain them:
api.add_resource(Demo15, '/demo15/<tkr>/<yr2predict>/<int:yrs2train>')
# curl localhost:5000/demo15/SPY/2017/1

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'

