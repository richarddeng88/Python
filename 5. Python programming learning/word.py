"""Retrive and print words from a URL

Usage:
    python word.py
"""

from urllib import urlopen
import sys
import pandas

def fetch_words_online(url):
    """Fetch a list of words from a URL.

    Args:
        url: the url of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the documents.
    """
    with urlopen(url) as story:
        story_word = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_word.append(word)

    for word in story_word:
        print word


def fetch_words_local(local_url):

    with open(local_url) as story:
        story_word = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_word.append(word)
    return story_word


def print_word(words):
    """Print items one per line

    Args:
        An iterable series of printable items.
    """
    for item in words:
        print item


def main():
    # url = sys.argv[1]
    local_url=sys.argv[1]
    words = fetch_words_local(local_url)
    print_word(words)

if __name__ == "__main__":
    main()
