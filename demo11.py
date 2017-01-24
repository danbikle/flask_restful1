# demo11.py

# This script should demonstrate:
# flask_restful.Resource
# flask_restful.Api
# api.add_resource()

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo11.py
# curl localhost:5000/demo11

import os
import flask
import flask_restful as fr

application = flask.Flask(__name__)
api         = fr.Api(application)

class Demo11(fr.Resource):
  def get(self):
    my_k_s = 'hello'
    my_v_s = 'world'
    return {my_k_s: my_v_s}
api.add_resource(Demo11, '/demo11')

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  application.run(host='0.0.0.0', port=port)
'bye'
