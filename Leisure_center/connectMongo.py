
from pymongo import MongoClient
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
mongoCnt = os.getenv('CLIENT_CONNECT')
mongoCollDB = os.getenv('COLLECT_DB')

# this is the string connection
client = MongoClient(mongoCnt)

mongoDB = client[mongoCollDB]

mongoColl = mongoDB['Course']

# docs = mongoColl.find()
# # pprint(docs)
# for aDoc in docs:
#     pprint(aDoc)


dbMongoClient = client[mongoCollDB]["Lessons"]
# coll = dbMongoClient.find_one({'CourseID':20})
# pprint(coll)

# print("\Looping through multiple documents\n")
# coll = dbMongoClient.find()
# for aDoc in coll:
#     pprint(aDoc)

    # print("\Insert Single document\n")
    # addDoc = dbMongoClient.insert_one({"CourseID": 000,"MemberID": 000})
    # print(addDoc.inserted_id)

# print("\Insert Single document\n")
# documents = [
# {'CourseID': 290, 'MemberID': 190 },
# {'CourseID': 230, 'MemberID': 220},
# {'CourseID': 270, 'MemberID': 282},
# {'CourseID': 1000, 'MemberID': 201}
# ]
 
# addDocs = dbMongoClient.insert_many(documents)
# print(addDocs.inserted_ids)

# print("\Update document\n")
# updateDoc = dbMongoClient.update_one({'CourseID': 270}, {'$set':{"MemberID":25000}})
# print(updateDoc.modified_count)

# print("\nUpdate Multiple documents\n")
# updateDocs = dbMongoClient.update_many({'MemberID': 15}, {'$set':{"CourseID":2111}})
# print(f"The number of updated documents: {updateDocs.modified_count}")
#
print("\nDelete single document")
deleteOne = dbMongoClient.delete_one({'CourseID':0})
print(f"Deleted: {deleteOne.deleted_count} document")

print("\nDelete multiple document")
deleteMany = dbMongoClient.delete_many({'CourseID':0})
print(f"Deleted: {deleteMany.deleted_count} documents")
