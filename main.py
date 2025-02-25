import sys

from stats import get_num_words
from stats import get_words_count
from stats import get_sorted_words_count

def get_book_text(filePath):
    with open(filePath, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        book_text = get_book_text(file_path)
    except:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    count = get_num_words(book_text)
    words_count = get_words_count(book_text)
    sorted_letters = get_sorted_words_count(words_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_letters:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")

main()
