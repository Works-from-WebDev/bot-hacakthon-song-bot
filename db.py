from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient()
db = client.get_database("sing_bot")
users = db.get_collection("users")


# Function to handle updates or inserts into the MongoDB database
def handle_update_or_insert(chat_id, user_name, score):
    document = {"chat_id": chat_id, "user_name": user_name, "score": score}
    users.update_one({"chat_id": chat_id}, {"$set": document}, upsert=True)


# Get all documents in the collection
documents = users.find()

# Iterate through the documents and print their contents
for document in documents:
    print(document)
