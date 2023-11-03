"""Boggler:  Boggle game solver. CS 210, Fall 2022.
Finn Fujimura.
Credits: TBD
"""
import doctest
import config
import data
import os

""""Configuration of Boggle player"""

# List of words to search for
DICT_PATH = "data/dict.txt"


def test_it():
    """A little extra work to keep text display from
    interfering with doctests.
    """
    saved_flag = config.TEXT_VIEW
    config.TEXT_VIEW = False
    doctest.testmod(verbose=True)
    config.TEXT_VIEW = saved_flag


def allowed(s: str) -> bool:
    """Is s a legal Boggle word?

    >>> allowed("am")  ## Too short
    False

    >>> allowed("de novo")  ## Non-alphabetic
    False

    >>> allowed("about-face")  ## Non-alphabetic
    False
    """
    if len(s) >= config.MIN_WORD and s.isalpha():
        return True
    else:
        return False


def normalize(s: str) -> str:
    """Canonical for strings in dictionary or on board
    >>> normalize("filter")
    'FILTER'
    """
    return s.upper()


def read_dict(path: str) -> list[str]:
    """Returns ordered list of valid, normalized words from dictionary.

    >>> read_dict("data/shortdict.txt")
    ['ALPHA', 'BED', 'BETA', 'DELTA', 'GAMMA', 'OMEGA']
    """

    words = []

    file_path = os.path.abspath(path)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                word = line.strip()
                if allowed(word):
                    normword = normalize(word)
                    words.append(normword)
        words.sort()
        return words
    else:
        return []


def main():
    pass


if __name__ == "__main__":
    test_it()
    main()
result = read_dict("data/shortdict.txt")
print(result)
