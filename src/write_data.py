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

# Writes data from the CSV file to the PostgreSQL database
def write_data_to_db(csv_file, table_name, conn):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Insert data into the database table
    for index, row in df.iterrows():
        cursor.execute(sql.SQL("""
            INSERT INTO {} (name, s1901_c01_012e, state, county)
            VALUES (%s, %s, %s, %s)
        """).format(sql.Identifier(table_name)), (row['NAME'], row['S1901_C01_012E'], row['state'], row['county']))

    # Commit the transaction
    conn.commit()

    # Close the cursor
    cursor.close()

# Main script
if __name__ == '__main__':

    # CSV file path
    csv_file_path = 'median_income_by_county.csv'

    # Database table name
    table_name = 'median_income_by_county'

    # Connect to the PostgreSQL database
    conn = connect_to_db()

    try:
        # Write data from CSV to PostgreSQL database
        write_data_to_db(csv_file_path, table_name, conn)
        print("Data written to PostgreSQL database successfully.")
    finally:
        # Close the database connection
        conn.close()