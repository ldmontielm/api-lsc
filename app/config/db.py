from pymongo import MongoClient

conn = MongoClient('mongodb+srv://admin:admin@container.qdz4bit.mongodb.net/?retryWrites=true&w=majority')

db = conn.dictionary
dbUsers = db.users