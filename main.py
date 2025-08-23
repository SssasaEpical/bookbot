# This function retrieves the book
path = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words():
    book_text = get_book_text(path)
    list_words = book_text.split()
    return len(list_words)

def main(path):
    pass

print(f"{count_words()} words found in the document")
