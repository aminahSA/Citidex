from flask import Flask, jsonify, request
from src import retrieve_county_info
from urllib.parse import urlparse
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
url = urlparse('postgres://u8rksns7e0ue9o:p9f315f6fb590af888dfa3acff321ee7f56970147ebeb53ffed115f88f86bfd22@ce0lkuo944ch99.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d962ts7irs7mfr')
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

# Route for getting data
@app.route('/api/data', methods=['GET'])
def get_data():    
    # Connect to the database through Heroku credentials
    conn = None
    try:
        conn = psycopg2.connect(
            dbname= dbname,
            user= user,
            password= password,
            host= host,
            port= port)
        
        # Open a cursor to perform database operations
        cursor = conn.cursor()
        # Retrieve income data from the median income table
        cursor.execute("SELECT * FROM median_income_by_county")
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        # Close the cursor
        cursor.close()
        return jsonify(rows)
    
    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({'error': str(e)}), 500
    
    finally:
         # Close the database connection
        if conn is not None:
            conn.close()

    # Example data
    #data = {'message': 'Hello from Flask'}
    #return jsonify(data)

# Route for posting data
@app.route('/api/data', methods=['POST'])
def post_data():
    posted_data = request.json
    # Process the posted data here
    return jsonify({'status': 'success', 'received': posted_data})

# Route for landing page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# have a route for the home page
@app.route('/home')
def home_display():
    pass

#route to handle form submission
@app.route('/form_submitted')
def form_display():
    pass


#route to display the results.


# Run the Flask application
if __name__ == '__main__':
    app.run()