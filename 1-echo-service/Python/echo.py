from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# HTTP (post) echo endpoint
@app.route('/', methods=['POST']) 
def echo():
    
    # Retrieve the data from the POST request
    data = request.json

    # Return the same data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="localhost", port=8090)

