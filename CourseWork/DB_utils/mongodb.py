import pymongo
from DB_utils.db_manager import DBManager

client = pymongo.MongoClient('localhost', 27017)
db = client['mongodb-server']

mongo_manager = DBManager(db['db-coursework-data'])

