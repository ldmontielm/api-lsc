from pymongo import MongoClient

conn = MongoClient('mongodb+srv://admin:admin@container.qdz4bit.mongodb.net/?retryWrites=true&w=majority')

# Base de datos
db = conn.dictionary
# Documentos
dbUsers = db.users
dbFields = db.fields
dbCategories = db.categories
dbPlaces = db.places
dbWords = db.words

