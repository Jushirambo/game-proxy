from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/games', methods=['GET'])
def get_games():
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/filter?tag=3d.mmorpg.fantasy.pvp&platform=pc'
    headers = {
        'x-rapidapi-key': '32acec076emsh69f4788d6f8bbabp116130jsnf0a8026f8325',
        'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
