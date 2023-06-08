from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient('mongodb://172.26.0.6')

# Access the "Tutorial1" database
db = client['Tutorial1']

# Insert a document into the "orders" collection
db.orders.insert_one({'test': 1})

# Close the connection
client.close()
