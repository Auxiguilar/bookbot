def count_book_words(text):
    return len(text.split())


def count_book_letters(text):
    letter_count = {}

    for t in text.lower():
        if t not in letter_count:
            letter_count[t] = 1
        else:
            letter_count[t] += 1

    return letter_count


def make_letter_list(letter_count): # just makes appropriate list out of letter_count
    letter_list = []

    for letter in letter_count:
        letter_list.append({"letter": letter, "num": letter_count[letter]})

    return letter_list


def sort_on(letter_list):
    return letter_list["num"]
