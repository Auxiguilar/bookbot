from stats import count_book_words, count_book_letters, make_letter_list, sort_on

def get_book_text(book_path):
    with open(book_path) as b:  # mysterious automatic opening and closing of file
        text = b.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_book_words(book_text)
    letter_count = count_book_letters(book_text)
    letter_list = make_letter_list(letter_count)
    letter_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for letter in letter_list:
        if letter["letter"].isalpha() == False:
            pass
        else:
            print(f"{letter["letter"]}: {letter["num"]}")
    
    print("============= END ===============")
    
main()

