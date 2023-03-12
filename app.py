# Import the Flask Dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/about')
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

    