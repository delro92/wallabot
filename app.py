from flask import Flask, jsonify, request
from wallapop_bot import search_wallapop

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    search_term = request.args.get('search_term', 'laptop')  # Default search term
    results = search_wallapop(search_term)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
