# demo12.py

# This script should demonstrate:
# flask_restful.Resource
# flask_restful.Api
# api.add_resource()
# URL-path parameters

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo12.py
# curl localhost:5000/demo12/IBM/2017/30

import os
import flask
import flask_restful as fr

application = flask.Flask(__name__)
api         = fr.Api(application)

class Demo12a(fr.Resource):
  # I should tell get() about URL-path parameters:
  def get(self, tkr='AAPL', yr2predict=2016, yrs2train=25):
    k1_s = 'You want to predict'
    k2_s = 'For this year'
    k3_s = 'By learning from this many years'
    return {k1_s:tkr, k2_s:yr2predict, k3_s:yrs2train}
# I should declare URL-path parameters:
api.add_resource(Demo12a, '/demo12a/<tkr>/<yr2predict>/<yrs2train>')

class Demo12b(fr.Resource):
  # I should tell get() about URL-path parameters:
  def get(self, tkr='AAPL', yr2predict=2016, yrs2train=25):
    k1_s = '1. You want to predict'
    k2_s = '2. For this year'
    k3_s = '3. By learning from this many years'
    return {k1_s:tkr, k2_s:yr2predict, k3_s:yrs2train}
# I should declare URL-path parameters, and I should constrain them:
api.add_resource(Demo12b, '/demo12b/<tkr>/<int:yr2predict>/<int:yrs2train>')

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
