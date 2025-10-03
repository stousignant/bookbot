import sys
from stats import count_characters, count_words, sorted_list_of_characters

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    text = get_book_text(path_to_book)
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count ----------")
    character_count = count_characters(text)
    sorted_characters = sorted_list_of_characters(character_count)
    for char in sorted_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    main(path_to_book)