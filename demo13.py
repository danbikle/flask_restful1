# demo13.py

# This script should demonstrate:
# flask_restful.Resource
# flask_restful.Api
# api.add_resource()
# URL-path-tokens
# URL-parameters

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo13.py
# curl localhost:5000/demo13/IBM/2017/30?features=pctlag1,slope2,dow,moy
# The above URL has path-tokens: IBM/2017/30
# The above URL has a URL-parameter named 'features'
import os
import flask         as fl
import flask_restful as fr

application = fl.Flask(__name__)
api         = fr.Api(application)

class Demo13(fr.Resource):
  # I should tell get() about URL-path-tokens:
  def get(self, tkr='AAPL', yr2predict=2016, yrs2train=25):
    features = fl.request.args.get('features', 'pctlag1') # pctlag1 is default
    k1_s = '1. You want to predict'
    k2_s = '2. For this year'
    k3_s = '3. By learning from this many years'
    k4_s = '4. With these features'
    return {k1_s:tkr, k2_s:yr2predict, k3_s:yrs2train, k4_s:features}
# I should declare URL-path-tokens, and I should constrain them:
api.add_resource(Demo13, '/demo13/<tkr>/<int:yr2predict>/<int:yrs2train>')
# curl localhost:5000/demo13/IBM/2017/30?features=pctlag1,slope2,dow,moy

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
