# This function retrieves the book
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# This function utilizes the get_book_text(filepath) funciton to print its contents
def main(path):
    print(get_book_text(path))

path = "books/frankenstein.txt"

main(path)
