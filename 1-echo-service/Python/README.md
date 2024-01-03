# Echo Service Using Python-Flask

## Use case

When the service is invoked with a message, the service will respond with the same message received via an HTTP POST.

## How to Run

`python -m pip install flask`
`python echo.py`
OR Using default port: 5000
`python -m flask --app echo run`

## Test the endpoint

```
curl -L 'http://localhost:8090/' -H 'Content-Type: application/json' -d '"Hello Word!"'
```
