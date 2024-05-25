import pandas as pd
import psycopg2
from psycopg2 import sql

# Connects to the database with the necessary parameters
def connect_to_db():
    conn = psycopg2.connect(
        dbname= 'Cost_of_living_data',
        user= 'postgres',
        password= '8395',
        host='localhost',
        port= '5432'
    )
    return conn

# Queries the database for a specific row/rows
def get_county_data(conn):

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Retrieve income data from the median income table
    cursor.execute("SELECT * FROM median_income_by_county")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor
    cursor.close()

# Main script
if __name__ == '__main__':
    # Connect to the PostgreSQL database
    conn = connect_to_db()
    
    try:
        # Retrieve data from PostgreSQL database
        get_county_data(conn)
        print("Data successfully retrieved.")
    finally:
        # Close the database connection
        conn.close()