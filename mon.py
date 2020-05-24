#!/usr/bin/python
from datetime import datetime
import os
import fnmatch
from pymongo import MongoClient

def main():
    #Time setup
    now = datetime.now()
    localtime = (now.strftime("%b-%d-%Y")).lower()

    # Connection Mongodb
    conn = MongoClient()

    total_user = ""
    total_bandwidth = 0.0

    # Database Bandwidth List
    not_list = ["admin", "local", "config"]

    for db_name in (conn.database_names()):
        if db_name not in not_list:

            # Database Name
            db = conn[db_name]

            # Collection Name
            collection = db[str(localtime)]

            # MAC Address Count
            total_user = collection.count()

            # Amount of Bandwidth
            for index in (collection.distinct('Bandwidth')):
                total_bandwidth = (total_bandwidth+float(index[:-3]))

            if total_user == 0:
                # Add New Collections 0 Total User & 0 Total Bandwidth
                post = {"Date" : "{}".format(localtime), "Total All User" : "{} User".format(total_user), "Total Bandwidth Usage" : "0 MB"}
                collection.insert_one(post)

                # Export to CSV
                os.system("mongoexport --db {} --collection {} --type=csv --fields MAC,Bandwidth,\'\',Date,\'Total All User\',\'Total Bandwidth Usage\' --out /home/hotspot-user/{}/{}_{}.csv".format(db_name, localtime, db_name, db_name, localtime))

            else:
                # Add New Field Total User & Total Bandwidth
                first = collection.find_one({})["MAC"]
                collection.update(
                    {"MAC" : "{}".format(first)},
                    {"$set" : {"Date" : "{}".format(localtime),
                     "Total All User" : "{} User".format(total_user),
                     "Total Bandwidth Usage" : "{} MB".format(total_bandwidth)}})

                # Export to CSV
                os.system("mongoexport --db {} --collection {} --type=csv --fields MAC,Bandwidth,\'\',Date,\'Total All User\',\'Total Bandwidth Usage\' --out /home/hotspot-user/{}/{}_{}.csv".format(db_name, localtime, db_name, db_name, localtime))

    # Telegram notif
    #os.system("curl -s -X GET \"https://api.telegram.org/bot"Bot ID"/sendMessage\" -d chat_id=\"Chat ID\" -d parse_mode=Markdown -d text=\"Monitoring Bandwidth Hotspot User Done\"")
    os.system("curl -s -X GET \"https://api.telegram.org/bot834874455:AAHIHpzbFdIMJu8TOnkKOCWjL8gelVJEa7c/sendMessage\" -d chat_id=\"-1001384805403\" -d parse_mode=Markdown -d text=\"Monitoring Bandwidthnya Done Ya Mas...\"")
if __name__ == '__main__':
    main()
