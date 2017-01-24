# demo10.py

# This script should allow me to serve a json file from the static folder.
# I should only need to import os and flask.

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python demo10.py
# Other terminal:
# curl localhost:5000/static/hello.json

import os
import flask

application = flask.Flask(__name__)
                       
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'
