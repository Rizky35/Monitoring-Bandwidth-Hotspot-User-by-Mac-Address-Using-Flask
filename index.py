#!/usr/bin/python
import fnmatch
import os
#from app import app
from flask import render_template
from flask import request
from flask import Flask
from pymongo import MongoClient
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def intro():

    #Testing
    return '''
<html>
    <head>
        <title>Monitoring MAC</title>
    </head>
    <body>
        <h1>Coba klik ini <a href=\"http://localhost:5000/index?username=Rizky&bandwidth=100000000&mac=6C:71:D9:7A:D7:83\">http://localhost:5000/index?username=Rizky&bandwidth=100000000&mac=6C:71:D9:7A:D7:83</a></h1>
    </body>
</html>'''

@app.route('/index', methods=['GET', 'POST'])
def index():

    # Variable from HTTP method=GET
    username = request.args.get('username')
    bandwidth = request.args.get('bandwidth')
    bandwidth_float = float(bandwidth) / 1024 / 1024
    bandwidth_str = (str(bandwidth_float)[:str(bandwidth_float).index(".")+2])
    mac = request.args.get('mac')

    # Time
    now = datetime.now()
    localtime = (now.strftime("%b-%d-%Y")).lower()

    # Connection Mongodb
    conn = MongoClient()

    # Database
    db = conn[username]

    # Collection
    collection = db[str(localtime)]

    # MAC Address Count
    mac_count = collection.count({"MAC" : "{}".format(mac)})

    # Add MAC Address
    if mac_count == 0:
        post = {"MAC" : "{}".format(mac), "Bandwidth" : "{} MB".format(bandwidth_str)}
        collection.insert_one(post)
        #print "New User"
        new = {"MAC" : "{}".format(mac), "Bandwidth" : "{}".format(bandwidth_str)}
        return new
    # Update Database from existing MAC Address
    else:
        bandwidth_dict = collection.find_one({"MAC" : "{}".format(mac)})
        bandwidth_exist = float(bandwidth_dict["Bandwidth"][:-3])
        bandwidth_new = float(bandwidth_str)

        # Update Database
        collection.update_one(
            {"MAC" : "{}".format(mac)},
            {"$set" : {"Bandwidth" : "{} MB".format(bandwidth_exist+bandwidth_new)}})
        #print "Append existing User"
        exist = {"MAC" : "{}".format(mac), "Bandwidth" : "{}".format(bandwidth_exist+bandwidth_new)}
        return exist

if __name__ == "__main__":
    #app.run()
    app.run(host= "0.0.0.0")
    #app.run(port= "80")
