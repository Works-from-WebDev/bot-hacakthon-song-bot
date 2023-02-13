from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient()
db = client.get_database("sing_bot")
users = db.get_collection("users")

# Delete all documents in the collection
users.delete_many({})


# Function to handle updates or inserts into the MongoDB database
def handle_update_or_insert(chat_id, user_name, score):
    document = {"chat_id": chat_id, "user_name": user_name, "score": score}
    users.update_one({"chat_id": chat_id}, {"$set": document}, upsert=True)


# Example usage of the function
handle_update_or_insert("chat1", "User 1", 100)
handle_update_or_insert("chat2", "User 2", 95)
handle_update_or_insert("chat1", "Updated User 1", 120)

# Get all documents in the collection
documents = users.find()

# Iterate through the documents and print their contents
for document in documents:
    print(document)
