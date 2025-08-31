def count_book_words(text):
    return len(text.split())


def count_book_characters(text):
    character_count = {}

    for char in text.lower():
        if char.isalpha():  # now only alphabeticals
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
    
    return character_count


def make_character_list(character_count): # just makes appropriate list out of letter_count
    character_list = []

    for char in character_count:
        character_list.append({"char": char, "num": character_count[char]})

    return character_list


def sort_on(character_list):
    return character_list["num"]
