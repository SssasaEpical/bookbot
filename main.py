from stats import count_words
from stats import count_characters
from stats import path
# This function retrieves the book

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analazing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words()} total words")

main(path)
