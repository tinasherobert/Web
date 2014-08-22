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
    app.run(debug = True)
