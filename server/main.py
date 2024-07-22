from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/users", methods=['Get'])
def users():
    return jsonify (
        {
            "users": [
                'kgen',
                "super",
                "tramp"
            ]
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=7180)