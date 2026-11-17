
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=10000)
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")

except Exception as e:
    print("MongoDB Connection Failed:", e)

finally:
    if "client" in globals():
        client.close()
