from unittest import TestCase, mock

from jsonschema.exceptions import ValidationError

import app as application
from app import app as flask_app


class TestSearch(TestCase):
    def setUp(self):
        flask_app.config['TESTING'] = True
        self.client = flask_app.test_client()

    def test_validation_failure(self):
        with mock.patch.object(application, 'validate_board_search', side_effect=ValidationError('invalid')):
            response = self.client.post('/v1/search')
        self.assertEqual(response.json, {'error': 'invalid'})
        self.assertEqual(response.status_code, 404)

    def test_success(self):
        with mock.patch.object(
            application, 'validate_board_search'
        ) as mock_validate:
            with mock.patch.object(
                    application, 'get_words_present_in_board', return_value={'a': True}
            ) as mock_get_words:
                response = self.client.post('/v1/search', json={
                    'words': ['a'],
                    'board': ['a'],
                }
                                            )
        self.assertEqual(response.json, {'a': True})
        self.assertEqual(response.status_code, 200)


class TestIntegrationSearch(TestCase):
    def setUp(self):
        flask_app.config['TESTING'] = True
        self.client = flask_app.test_client()

    def test_success(self):
        response = self.client.post(
            '/v1/search',
            json={
                'words': ['a'],
                'board': ['a'],
            }
        )
        self.assertEqual(response.json, {'a': True})
        self.assertEqual(response.status_code, 200)
