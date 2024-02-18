from dotenv import load_dotenv
import os, mysql.connector

load_dotenv()
passkey1 = os.getenv('sql_pass')
__dbCon = None

def get_sql_connection():
    global __dbCon
    if __dbCon is None:
        __dbCon = mysql.connector.connect(user = 'root',
                                        host = 'localhost',
                                        password = passkey1,
                                        database = 'grocery_store')
    return __dbCon