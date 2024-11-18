# from pymongo import MongoClient

# # 如果MongoDB安装在本地则改成localhost,否则改成MongoDB所在的电脑或服务器的IP地址
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

# 如果MongoDB安装在本地则改成localhost,否则改成MongoDB所在的电脑或服务器的IP地址
mongodb_host = os.getenv("MONGO_URI", "mongodb://root:root@localhost:27017/")
print(mongodb_host)

# json文件加了方括号[]

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
