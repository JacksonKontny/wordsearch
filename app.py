import json

from flask import Flask
from flask import make_response
from flask import request
from jsonschema.exceptions import ValidationError

from validation import validate_board_search
from word_search import get_words_present_in_board


app = Flask(__name__)
 

@app.route('/v1/search', methods=['POST'])
def search():
    try:
        validate_board_search(request.json)
    except ValidationError as exception:
        return _get_json_response({'error': str(exception)}, 404)
    board = request.json.get('board')
    words = request.json.get('words')
    return _get_json_response(get_words_present_in_board(board, words), 200)


def _get_json_response(response_dict, status_code):
    return app.response_class(
        response=json.dumps(response_dict),
        status=status_code,
        mimetype='application/json'
    )
 
if __name__ == "__main__":
    app.run()
