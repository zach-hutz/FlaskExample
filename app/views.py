from app import app
from flask import render_template, jsonify, request
import json

# Displaying a HTML page by returning render template
@app.route('/')
def index():
    return render_template('index.html')


# Displaying JSON data
@app.route('/data', methods=['GET', 'POST'])
def swapCase():
    # Post method
    if request.method == 'POST':
        data = request.get_json()['data']
        data = str(data).upper()
        print(data)
        return jsonify({'upper': data})
    else:
        # Get Method
        myData = 5
        return jsonify({'data': myData})

# Displaying an HTML page with data by returning render template
@app.route('/jinja')
def jinja():
    myData = 10
    return render_template('jinja.html', data=json.dumps(myData))

