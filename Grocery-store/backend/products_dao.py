from dotenv import load_dotenv
from sql_connect import get_sql_connection
import os

load_dotenv()


def get_all_gsproducts(connection):
    cursor = connection.cursor()
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

    return responce

def insert_new_gsproduct(connection, product):
    cursor = connection.cursor()
    query =("INSERT INTO products "
          "(name, uom_id, price_per_unit)"
          "values (%s, %s, %s)")
    data = (product['name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_gsproduct(connection, product_id):
    cursor = connection.cursor()
    query =(f"DELETE FROM products where product_id={product_id}")
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_gsproduct(connection, 13))
    print("Product successfully deleted")

# if __name__ == '__main__':
#     connection = get_sql_connection()
#     print(insert_new_product(connection, {
#         'name': 'bok choy', 
#         'uom_id': '1', 
#         'price_per_unit': '1.20' 
#     }))
    
# if __name__ == '__main__':
#     connection = get_sql_connection()
#     print(get_all_products(connection))