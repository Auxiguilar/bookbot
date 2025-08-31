from stats import count_book_words, count_book_characters, make_character_list, sort_on

def get_book_text(book_path):
    with open(book_path) as b:  # mysterious automatic opening and closing of file
        text = b.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_book_words(book_text)
    character_count = count_book_characters(book_text)
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
    main()

