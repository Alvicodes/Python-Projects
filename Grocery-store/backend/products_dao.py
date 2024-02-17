from dotenv import load_dotenv
import os, mysql.connector

load_dotenv()

passkey1 = os.getenv('sql_pass')

def get_all_products():
    try:
        dbCon = mysql.connector.connect(user = 'root',
                                        host = 'localhost',
                                        password = passkey1,
                                        database = 'grocery_store')

        cursor = dbCon.cursor()
        query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
                "FROM products INNER JOIN uom ON products.uom_id=uom.uom_id")

        cursor.execute(query)
        
        responce = []

        for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
            responce.append(
                {
                    'product_id': product_id,
                    'name': name, 
                    'uom_id': uom_id, 
                    'price_per_unit': price_per_unit, 
                    'uom_name': uom_name,
                    
                }
            )

        dbCon.close()
        
        return responce
    except mysql.connector.Error as err:
        print(f"Error connecting to: {err}")
        return []

if __name__ == '__main__':
    print(get_all_products())