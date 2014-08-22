#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tina
#
# Created:     13/06/2013
# Copyright:   (c) tina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from flask import *

app = Flask(__name__)

@app.route('/')
def index() :
    return "tinashe makaza tesing the website "

@app.route('/tinashe')
def tina():
	return "tinashe i see you "

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
