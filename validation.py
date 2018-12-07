import os

from bravado_core.spec import Spec
from bravado_core.validate import validate_object
from yaml import load, Loader, dump, Dumper
from jsonschema.exceptions import ValidationError


def validate_board_search(request_json):
    validate_object(SPEC, BOARD_SPEC, request_json)
    _validate_board(request_json['board'])
    _validate_words(request_json['words'])


def _validate_board(board):
    board_size = len(board)
    if not board_size:
        raise ValidationError('`board` must have more than 0 characters in it')
    for row in board:
        if len(row) != board_size:
            raise ValidationError('`board` dimensions must be equal (N X N)')


def _validate_words(words):
    if not len(words):
        raise ValidationError('`words` must contain at least one word')
    for word in words:
        if not word:
            raise ValidationError('all words in `words` must have at least one character')


def get_swagger_spec():
    with open(SPEC_PATH,'r') as spec:
        return load(spec.read(), Loader)


bravado_config = {
    'validate_swagger_spec': False,
    'validate_requests': False,
    'validate_responses': False,
    'use_models': True,
}

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
SPEC_PATH = os.path.join(DIR_PATH, "swagger.yml")
SPEC_DICT = get_swagger_spec()
SPEC = Spec.from_dict(SPEC_DICT, config=bravado_config)
BOARD_SPEC = SPEC_DICT['definitions']['BoardSearch']
