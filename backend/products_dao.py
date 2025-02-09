from sql_connection import get_sql_connection

# Fetching all the data in the products table of the grocery_store database
def get_all_products(connection):
    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # SQL query to retrieve product details by joining 'products' and 'uom' tables
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
            "FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")
    
    # Execute the query
    cursor.execute(query)
    # Initialize an empty list to store the query results
    response = []

    # Iterate through the result rows and convert each row into a dictionary
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,       # Unique product ID
                'name': name,                   # Product name
                'uom_id': uom_id,               # Unit of measure ID
                'price_per_unit': price_per_unit,  # Price per unit
                'uom_name': uom_name            # Unit of measure name
            }
        )
    # Return the list of products
    return response

# Inserting a new product into the products table in the database
def insert_new_product(connection, product):
    # Create a cursor object to execute queries
    cursor = connection.cursor()
    
    # SQL query to insert a new product into the 'products' table
    query = ("insert into products"
             "(name,uom_id,price_per_unit)"
             "values(%s,%s,%s)")
    
    # Data values for the query placeholders
    data = (product['product_name'],    # Product name
            product['uom_id'],          # Unit of measure ID
            product['price_per_unit'])  # Price per unit
    
    # Execute the query with the provided data
    cursor.execute(query, data)
    
    # Commit the changes to save the new product in the database
    connection.commit()
    
    # Return the ID of the newly inserted product
    return cursor.lastrowid

# Deleting a product from the products table in the database
def delete_product(connection, product_id):
    # Create a cursor object to execute queries
    cursor = connection.cursor()
    
     # SQL query to delete a product based on its product_id
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))

    # Execute the query
    cursor.execute(query)
    
    # Commit the changes to confirm the deletion
    connection.commit()
    
    return cursor.lastrowid
    
# Main entry point for the script
if __name__=='__main__':
     # Establish the connection to the database
    connection = get_sql_connection()
    """
    # Insert a new product and print its ID
    print(insert_new_product(connection, {
        'product_name': 'cabbage',  # Name of the product
        'uom_id': '1',              # Unit of measure ID
        'price_per_unit': '10'      # Price per unit
    }))
    """
    # Delete the product with ID 12 from the 'products' table and confirm the deletion
   # print(delete_product(connection, 13))
    
