from flask import Flask, request, jsonify
from flask_cors import CORS

# Step 1: Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Step 2: Define the route
@app.route('/generate-testcases', methods=['POST'])
def generate_testcases():
    data = request.get_json()
    code = data.get('code', '')

    # Dummy test case generation logic
    testcases = [
        "assert is_palindrome('madam') == True",
        "assert is_palindrome('hello') == False",
        "assert is_palindrome('Race car') == True",
        "assert is_palindrome('Was it a car or a cat I saw') == True"
    ]

    return jsonify({"testcases": testcases})

# Step 3: Run the app
if __name__ == '__main__':
    app.run(debug=True)
