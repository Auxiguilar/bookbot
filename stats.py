def count_book_words(text):
    word_count = 0

    for t in text.split():  # becomes a list and just works; dunno how. did suspect the possibility, and boots obliged
        word_count += 1
    
    return word_count

def count_book_letters(text):
    letter_count = {}

    for t in text.lower():  # iterating on a string is magical, wonderful, and unexpected
        if t not in letter_count:
            letter_count[t] = 1
        else:
            letter_count[t] += 1

    return letter_count

# letters = {}
# text = "This is a string."
# for t in text.lower():
#     if t not in letters:
#         letters[t] = 1
#     else:
#         letters[t] += 1
# print(letters)