from flask import Flask, request, jsonify

app = Flask(__name__) # Create a Flask app

# HTTP (post) echo endpoint
@app.route('/echo', methods=['POST']) 
def echo():
    # Retrieve the data from the POST request
    data = request.json

    # Return the same data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
