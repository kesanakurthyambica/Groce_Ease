# Importing the MySQL connector library for connecting to the MySQL database
import mysql.connector

# Global variable to store the connection object
__cnx = None

# Function to establish and return a connection to the MySQL database
def get_sql_connection():
    # Use the global variable __cnx to avoid creating multiple connections
    global __cnx

    # Check if a connection object already exists
    if __cnx is None:
        # If no connection exists, create a new connection
        __cnx = mysql.connector.connect(
            user='root',                   # The username for the database
            password='Ambica3014@',        # The password for the database
            host='localhost',              # The host (e.g., 'localhost' or the IP address of the server)
            port=3306,                     # The port MySQL is running on (default is 3306)
            database='grocery_store'       # The name of the database to connect to
        )
    
    # Return the connection object
    return __cnx
