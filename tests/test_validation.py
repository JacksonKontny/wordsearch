from unittest import TestCase, mock

from jsonschema.exceptions import ValidationError

import validation


class TestValidateBoardSearch(TestCase):
    def test_board_missing(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': ['word1']})
        self.assertEqual(ctx.exception.message, "'board' is a required property")

    def test_board_word_wrong_type(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': ['word1'], 'board': [1]})
        self.assertEqual(ctx.exception.message, "1 is not of type 'string'")

    def test_words_missing(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'board': []})
        self.assertEqual(ctx.exception.message, "'words' is a required property")
        pass

    def test_words_wrong_type(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': [1], 'board': []})
        self.assertEqual(ctx.exception.message, "1 is not of type 'string'")

    def test_empty_board(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': ['word1'], 'board': []})
        self.assertEqual(ctx.exception.message, "`board` must have more than 0 characters in it")

    def test_non_square_board(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': ['word1'], 'board': ['123', '12']})
        self.assertEqual(ctx.exception.message, "`board` dimensions must be equal (N X N)")

    def test_no_words(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': [], 'board': ['12', '12']})
        self.assertEqual(ctx.exception.message, "`words` must contain at least one word")

    def test_blank_word(self):
        with self.assertRaises(ValidationError) as ctx:
            validation.validate_board_search({'words': ['hello', ''], 'board': ['12', '12']})
        self.assertEqual(ctx.exception.message, "all words in `words` must have at least one character")

    def test_valid(self):
        self.assertIsNone(
            validation.validate_board_search(
                {'words': ['hello', 'goodbye'], 'board': ['12', '12']}
            )
        )
