from stats import get_num_chars
from stats import get_num_words
import sys
def get_book_text(path) -> str:
    a = ""
    with open(path) as f:
        file_contents = f.read()
        a = file_contents
    return a
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    p = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {get_num_words(p)} total words")
    print("--------- Character Count -------") 
    get_num_chars(p)
    print("============= END ===============")
if __name__ == "__main__":
    main()