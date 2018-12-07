from unittest import TestCase, mock

import word_search


class BaseTestWordSearch(TestCase):

    def setUp(self):
        self.board = ['FDOG', 'ICAT','SPIG','HANT']


class TestGetWordsPresentInBoard(BaseTestWordSearch):

    def test_check_for_word(self):
        with mock.patch.object(word_search, '_check_for_word', side_effect=[False, True]) as mock_check:
            words_present = word_search.get_words_present_in_board(self.board, ['call_one', 'call_two'])
        self.assertDictEqual(
            words_present,
            {'call_one': False, 'call_two': True}
        )
        mock_check.assert_any_call(self.board, 'call_one')
        mock_check.assert_any_call(self.board, 'call_two')


class TestCheckForWord(BaseTestWordSearch):

    def test_first_word_present(self):
        with mock.patch.object(word_search, '_row_wise_check_for_word', side_effect=[True, False]) as mock_check:
            self.assertTrue(word_search._check_for_word(self.board, 'word'))
        mock_check.assert_called_once_with(self.board, 'word')

    def test_second_word_present(self):
        with mock.patch.object(word_search, '_row_wise_check_for_word', side_effect=[False, True]) as mock_check:
            self.assertTrue(word_search._check_for_word(self.board, 'word'))
        mock_check.assert_any_call(self.board, 'word')
        self.assertEqual(mock_check.call_count, 2)

    def test_word_not_present(self):
        with mock.patch.object(word_search, '_row_wise_check_for_word', return_value=False) as mock_check:
            self.assertFalse(word_search._check_for_word(self.board, 'word'))
        mock_check.assert_any_call(self.board, 'word')
        self.assertEqual(mock_check.call_count, 2)


class TestTranspose(BaseTestWordSearch):

    def test_transpose(self):
        self.assertEqual(
            word_search._transpose(self.board),
            ['FISH', 'DCPA', 'OAIN', 'GTGT'],
        )


class TestRowWiseCheckForWord(BaseTestWordSearch):

    def test_word_present(self):
        self.assertTrue(word_search._row_wise_check_for_word(self.board, 'DOG'))

    def test_backwards_word_present(self):
        self.assertTrue(word_search._row_wise_check_for_word(self.board, 'GOD'))

    def test_word_not_present(self):
        self.assertFalse(word_search._row_wise_check_for_word(self.board, 'X'))
