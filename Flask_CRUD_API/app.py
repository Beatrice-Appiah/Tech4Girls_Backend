from flask import Flask, jsonify, request
from laptops_blueprint import laptops_blueprint

app = Flask(__name__)
app.register_blueprint(laptops_blueprint)


# The Endpoint for home
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Laptop Management API!"})


# Ensures that backend server runs
if __name__ == '__main__':
    app.run(debug=True)