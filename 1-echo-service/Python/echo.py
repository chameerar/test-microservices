from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return "Echo Service Running"

# HTTP (post) echo endpoint
@app.route('/', methods=['POST']) 
def echo():
    
    # Retrieve the data from the POST request
    data = request.json

    # Return the same data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8090)

