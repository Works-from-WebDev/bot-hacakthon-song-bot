from pymongo import MongoClient

# Connect to the MongoDB database

class Database:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.get_database("sing_bot")
        self.users = self.db.get_collection("users")

    def handle_update_or_insert(self, chat_id, user_name, score, games, guest_right=None, friends=None):
        self.document = {"chat_id": chat_id,
                        "user_name": user_name,
                        "history": {
                         "score": score,
                         "games": games
                     }}
        if guest_right is not None:
            self.document["history"]["guest_right"] = guest_right
        if friends is not None:
            self.document["friends"] = friends
        self.users.update_one({"chat_id": chat_id}, {
            "$set": self.document}, upsert=True)

    def get_all(self):
        documents = self.users.find()
        for document in documents:
            print(document)