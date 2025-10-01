from stats import get_num_words
from stats import get_num_char
from stats import sort_dict
import sys

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]

    content = get_book_text(path_to_book)
    num_words = get_num_words(content)
    num_char = get_num_char(content)
    last_list = sort_dict(num_char)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print(f"--------- Character Count -------")
    for item in last_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


main()
