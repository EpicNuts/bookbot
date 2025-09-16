import sys
from stats import word_count, char_count,sorted_list

def get_path_to_book():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]
    
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
      return file.read()

def main():
    filepath = get_path_to_book()

    book_text = get_book_text(filepath)

    num_words = word_count(book_text)
    num_chars = char_count(book_text)

    sorted_chars = sorted_list(num_chars)

    # print(sorted_chars)
    # print(f"{num_words} words found in the document")
    # print(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        for key, value in i.items():
            print(f"{key}: {value}")        

if __name__ == "__main__":
  main()

