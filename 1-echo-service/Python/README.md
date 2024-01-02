# Echo Service Using Python-Flask

# How to Run

'''python -m pip install flask
python -m flask --app echo run
'''

# Test the endpoint

curl --location 'http://127.0.0.1:5000/echo' \
--header 'Content-Type: application/json' \
--data '"Hello Word!"'
