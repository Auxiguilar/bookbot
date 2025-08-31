from stats import count_book_words, count_book_characters, make_character_list, sort_on
import sys

def get_book_text(path):
    with open(path) as b:  # mysterious automatic opening and closing of file
        text = b.read()
        return text

def main(path):
    text = get_book_text(path)
    word_count = count_book_words(text)
    character_count = count_book_characters(text)
    character_list = make_character_list(character_count)
    character_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in character_list:
        print(f"{char["char"]}: {char["num"]}")
    
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])

