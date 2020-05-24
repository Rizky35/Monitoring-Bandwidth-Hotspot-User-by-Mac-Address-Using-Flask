from datetime import datetime
from pymongo import MongoClient

def main():
    #Time setup
    now = datetime.now()
    localtime = (now.strftime("%b-%d-%Y")).lower()

    # Connection Mongodb
    conn = MongoClient()

    # Database Bandwidth List
    not_list = ["admin", "local", "config"]

    for db_name in (conn.database_names()):
        if db_name not in not_list:

        	# Database Name
            db = conn[db_name]

            # Collection Name
            collection = db[str(localtime)]

            # Add New Field Total User & Total Bandwidth
            first = collection.find_one({})["MAC"]
            collection.update(
                {"MAC" : "{}".format(first)},
                {"$unset" : {"Tanggal" : "",
                 "Total Seluruh User" : "",
                 "Total Seluruh Penggunaan Bandwidth" : ""}})

if __name__ == '__main__':
    main()