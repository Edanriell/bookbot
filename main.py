import sys

from stats import get_char_count
from stats import get_num_words
from stats import get_sorted_char_count


def get_book_text(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def analyze_text(text):
    """Processes text and returns word count and sorted character frequency."""
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    sorted_chars = get_sorted_char_count(char_count)
    return word_count, sorted_chars


def print_analysis(file_path, word_count, sorted_chars):
    """Prints the analysis results."""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_chars:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count, sorted_chars = analyze_text(book_text)
    print_analysis(file_path, word_count, sorted_chars)


if __name__ == "__main__":
    main()
