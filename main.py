from stats import count_book_words, count_book_letters

def get_book_text(book_path):
    with open(book_path) as b:  # mysterious automatic opening and closing of file
        text = b.read()
        return text

    
def main():
    book_text = get_book_text("books/frankenstein.txt") # var = return value from func. very useful; now main can do the printing work
#    print(book_text)

#    print(get_book_text("books/frankenstein.txt"))

#    book_words = count_book_words(book_text)
#    print(f"{book_words} words found in the document")
    print(f"{count_book_words(book_text)} words found in the document")

#    book_letters = count_book_letters(book_text)
#    print(book_letters)
    print(f"{count_book_letters(book_text)}")

main()

