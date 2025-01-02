from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

# Create a new client and connect to the server
client = MongoClient(os.getenv('MONGODB_URL'), server_api = ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
myDB = client[os.getenv('DATABASE')]
myCL = myDB[os.getenv('COLLECTION')]

print("歡迎使用圖書館查詢系統")
while(True):
    print("請選擇查詢方式 1.查詢作者 2.查詢書名 3.查詢借閱次數 4.結束查詢")
    num = input()

    if num == "1":
        author = input("請輸入作者名稱:")
        query = {"Authors":{"$in":[author]}}
        results = myCL.find(query)
        print(f"作者為「{author}」的書:")
        for document in results:
            print(document["Title"])
        print("\n")

    elif num == "2":
        searchkeyword = input("請輸入書名關鍵字:")
        query = {"Title":{"$regex":searchkeyword}}
        results = myCL.find(query)
        print(f"含有「{searchkeyword}」的書:")
        for document in results:
            print(document["Title"])
        print("\n")

    elif num == "3":
        title = input("請輸入書名:")
        query = {"Title": {"$eq":title}}
        results = myCL.find(query)
        print(f"書名為「{title}」的借閱次數:")
        for document in results:
            print(str(document["BorrowCount"]) + "次")
        print("\n")

    elif num == "4":
        print("\n")
        break
    else:
        print("輸入錯誤，請重新輸入🙄")
        print("\n")

print("感謝使用圖書館系統😊")

client.close()

