
from flask import Flask, jsonify, request
from src import retrieve_county_info

app = Flask(__name__)

# Route for getting data
@app.route('/api/data', methods=['GET'])
def get_data():
    # Try to receive data from the database using rci module
    try:
        conn = retrieve_county_info.connect_to_db()
        rows = retrieve_county_info.get_county_data(conn)
        return jsonify(rows)
    finally:
        # Close the database connection
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