import pymongo
from pymongo import MongoClient

import pandas as pd

import json
import sys

print("Select One : ")
print("1. Create random dummy data ")
print("2. Import csv/JSON data to database ")
tmp = int(input())


if tmp == 1 :
    pass
elif tmp == 2 :
    print("-------------------------------------------------------------------")
    print("Input --host , --port ")
    print("default localhost is ( localhost:27017 ) ")
    
    host,port = sys.stdin.readline().split()
    
    try :	 
    	client = MongoClient(host= host, port= int(port))
    except :
	print("Connection Failed, Retry with correct host and port")
	exit(1) 


    print('input database-name , collection-name')
    dbname , collectionname = sys.stdin.readline().split() # error can occur Careful
    db = client.get_database(dbname)
    cl = db.get_collection(collectionname)

    

    print('input file path ')
    path = sys.stdin.readline()
    path = path[:-1] # erase EOF char
    if path[-3:] == 'csv' :
        try :
	    try :
	    	file = pd.read_csv(path,encoding="utf-8")
            except :
		exit(1)
	    data = file.to_dict()
	    cl.insert_many(data)
    	except:
	    print('error occur in inserting, plz try again')

    elif path[-4:] == 'json' :
        with open(path,"r", encoding="utf-8") as file :
            file_data = json.load(file)
        if isinstance(file_data, list) :
            cl.insert_many(file_data)
        else :
            cl.insert_one(file_data)
    else :
	print(path[-3:]) 
    print("finished.")
    exit(0)

else :
    print("plz input correct num ( 1 or 2 ) ")
    exit(1)
