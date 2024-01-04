from flask import Flask, request

# Create a Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return "Echo Service Running"

# HTTP (POST) echo endpoint
@app.route('/', methods=['POST'])
def echo():
    # Retrieve the data from the POST request
    data = request.data.decode('utf-8')

    # Return the same data as plain text
    return data, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(port=8090)
