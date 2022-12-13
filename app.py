from flask import Flask, jsonify, render_template, redirect, url_for, make_response
from flask_cors import CORS

import json
from genAnalytics import generate_report
from flask_mysqldb import MySQL


SALES = []


# configuration
DEBUG = True
 
# instantiate the app
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sales_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.config.from_object(__name__)
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
 
 
# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('ping~')
 
@app.route('/sales', methods=['GET'])
def getSales():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM sales_tbl WHERE 1 LIMIT 0, 20")
    sales = cursor.fetchall()
    return make_response(jsonify(sales), 200)

@app.route('/report')
def showReport():
    return render_template("generated_report.html")

@app.route('/generate')
def run_script():
    generate_report()
    return redirect(url_for('showReport'))

 
if __name__ == '__main__':
    app.run()