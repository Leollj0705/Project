# from pymongo import MongoClient

# If MongoDB is installed locally, change it to localhost, otherwise change it to the IP address of the computer or server where MongoDB is located.
# mongodb_host = 'mongodb://localhost:27017/'

# # mongodb_host = 'mongodb://192.168.1.9:27017/'
# database_name = 'ecom'
# ecom_collection = 'ecom_collection'
# users_collection = 'users_collection'
# login_attempts_collection = 'login_attempts_collection'

# client = MongoClient(mongodb_host)
# ecom_db = client[database_name]
# ecom_collection = ecom_db[ecom_collection]
# users_collection = ecom_db[users_collection]
# login_attempts_collection = ecom_db[login_attempts_collection]

from pymongo import MongoClient
import os

# If MongoDB is installed locally, change it to localhost, otherwise change it to the IP address of the computer or server where MongoDB is located.
mongodb_host = os.getenv("MONGO_URI", "mongodb://root:root@localhost:27017/")
print(mongodb_host)

# The json file is enclosed in square brackets [].

# mongodb_host = 'mongodb://192.168.1.9:27017/'
database_name = 'ecom'
ecom_collection = 'ecom_collection'
users_collection = 'users_collection'
login_attempts_collection = 'login_attempts_collection'


client = MongoClient(mongodb_host)
ecom_db = client[database_name]
ecom_collection = ecom_db[ecom_collection]
users_collection = ecom_db[users_collection]
login_attempts_collection = ecom_db[login_attempts_collection]
