from flask import Flask, render_template, request, session, make_response

import pandas as pd
import quandl
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.charts import TimeSeries, show, output_file
from bokeh.plotting import *

#output_notebook()

app = Flask(__name__)


#-------- ROUTES GO HERE -----------#

# This method takes input via an HTML page


@app.route('/')
def stocks():
   return render_template('index.html')

@app.route('/reports', methods=['POST','GET'])
def result():
    '''Gets prediction using the HTML form'''
    if request.method == 'POST':
        stock = request.form['query']    


    col   =['Open', 'Close']
    rows=300

    stock_code = "WIKI/"+stock

    mydata = quandl.get(stock_code, rows=rows)

    fig = TimeSeries(mydata,y=col, 
                title="Stock Prices for "+stock, 
                ylabel='Stock Prices', xlabel='Last '+str(rows)+' days',
                legend='top_left')

    save(fig, filename="./templates/graph.html")
    show(fig)
    return(render_template('graph.html'))


if __name__ == '__main__':
    app.run()
