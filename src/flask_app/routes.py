from flask_app import app
from flask import Flask, jsonify, request


# Route for getting data
@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data
    data = {'message': 'Hello from Flask'}
    return jsonify(data)

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