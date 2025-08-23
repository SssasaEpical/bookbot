path = "books/frankenstein.txt"
# Obtains contents from file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words():
    book_text = get_book_text(path)
    list_words = book_text.split()
    return len(list_words)

def count_characters():
    characters_total = {}
    book = get_book_text(path)
    book = book.lower()
    for characters in book:
        if characters not in characters_total:
            characters_total[characters] = 1
        else:
            characters_total[characters] += 1
    print(characters_total)
