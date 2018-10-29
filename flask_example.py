from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_restful import Api
import csv
import json
from dateutil.parser import parse
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)
api = Api(app)

def filter(start, end, country, title):
    
    # read csv file into pandas dataframe
    df = pd.read_csv('tvav_test-files/epg.csv')
    
    # compute start_time and end_time for each row
    df['start'] = df[['start_date']].applymap(str).applymap (lambda s: "{}/{}/{}".format(s[0:4], s[4:6], s[6:]))
    df['start'] = pd.to_datetime(df['start'] + ' ' + df['start_time'])
    df['end'] = df['start'] + pd.to_timedelta(df['duration_in_seconds'], unit='s')
    
    # create and format start_time and end_time fields for report
    df['start_time'] = df['start'].dt.strftime('%Y%m%d - %H:%M')
    df['end_time'] = df['end'].dt.strftime('%Y%m%d - %H:%M')
    
    # select records between dates in arguments
    df = df[(df['start'] >= start) & (df['end'] <= end)]
    
    # if country was specified in arguments, delete the rows not in it
    if country != None:
        df = df[(df['channel_country'] == country)]
    
    # if title was specified, delete the records without the title
    if title != None:
        df = df[(df['program_original_title'] == title)]
    
    # delete temporary columns
    df.drop('start', axis=1)
    df.drop('end', axis=1)

    return df

@app.route('/form', methods=['GET'])#, 'POST'])
def form_get():

    # draws boxes to input data
    return '''<form method="POST">
        Start Date (yyyymmdd) (mandatory): <input type="text" name="start"><br>
        End Date (yyyymmdd) (mandatory): <input type="text" name="end"><br>
        Country (TLA) (optional): <input type="text" name="country"><br>
        Title (optional): <input type="text" name="title"><br>
        <input type="submit" value="Submit"><br>
        </form>'''

@app.route('/form', methods=['POST'])
def form_post():
    
    #read parameters from url into variables (depending on method)
    if request.method == 'POST': # form
        start = parse(request.form['start'])
        end = parse(request.form['end'])
        if request.form['country'] == '':
            country = None
        else:
            country = request.form['country']
        if request.form['title'] == '':
            title = None
        else:
            title = request.form['title']
        print(start, end, country, title)
        return filter(start, end, country, title).to_html()

@app.route('/query')
def query():
    
    #read parameters from url into variables
    start = parse(request.args.get('start'))
    end = parse(request.args.get('end'))
    country = request.args.get('country')
    title = request.args.get('title')
    print(start, end, country, title)
    
    # return selected rows in json format
    return(filter(start, end, country, title).to_json(orient='records'))

app.run(debug=True)

