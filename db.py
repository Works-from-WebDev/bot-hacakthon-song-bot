from pymongo import MongoClient

# Connect to the MongoDB database


class Database:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.get_database("sing_bot")
        self.users = self.db.get_database("users")
# client = MongoClient()
# db = client.get_database("sing_bot")
# users = db.get_collection("users")


# Function to handle updates or inserts into the MongoDB database


    def handle_update_or_insert(self, chat_id, user_name, score):
        self.document = {"chat_id": chat_id,
                         "user_name": user_name, "score": score}
        self.users.update_one({"chat_id": chat_id}, {
                              "$set": self.document}, upsert=True)

    def get_all(self):
        return self.users.find()


# Get all documents in the collection
# documents = users.find()

# Iterate through the documents and print their contents
# for document in documents:
#     print(document)


"""
friends 
score --> histoty 

history = {
    score,
    games,
    gueest_right,
    



"""
