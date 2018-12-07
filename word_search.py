
# Assumptions:
## Board does not take up a considerable portion of memory

def get_words_present_in_board(board, words):
    words_present = {}
    for word in words:
        words_present[word] = _check_for_word(board, word)
    return words_present


def _check_for_word(board, word):
    return (
        _row_wise_check_for_word(board, word)
        or _row_wise_check_for_word(_transpose(board), word)
    )


def _transpose(board):
    return [''.join(s) for s in zip(*board)]


def _row_wise_check_for_word(rows, word):
    backwards_word = ''.join(reversed(word))
    for row in rows:
        if word in row or backwards_word in row:
            return True
    return False
