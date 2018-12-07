# Wordsearch
Microservice for searching for words in a matrix


## Wordsearch Development

Wordsearch developed using Python 3.6.5 and the flask microframework.

To get started:

```bash
pip install -r requirements.txt
python app.py
```

To run tests:

```
python -m unittest discover
```

## Assumptions

1. The board is not too large to fit into memory
1. The word search program is case sensitive
1. Diagonals are not searched
1. Backwards words are searched
1. Numbers, spaces and special characters are allowed

## Future Work

1. Optimize word search algorithm to loop through characters in board one time
1. Optimize word search to only check for matches in directions that are large enough for word to fit
1. Do not search for words that are larger than N (the size of the board)
1. Perhaps search for diagonals
