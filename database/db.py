# database/db.py

from pymongo import MongoClient

def get_db():
    """
    Connects to the local MongoDB server and returns
    the 'certificate_db' database object.
    Falls back safely if connection fails.
    """
    try:
        # Local MongoDB URI (can be replaced with env variable later)
        uri = "mongodb://localhost:27017"
        client = MongoClient(uri)

        # Connect to or create the database
        db = client["certificate_db"]
        return db

    except Exception as e:
        print("❌ MongoDB connection failed:", e)
        return None
