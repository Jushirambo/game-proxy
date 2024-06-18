from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/games', methods=['GET'])
def get_games():
    url = 'https://www.freetogame.com/api/games?sort-by=alphabetical'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
