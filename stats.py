def get_num_words(text):
    num_words = len(text.split())

    return num_words

def get_words_count(text):
    characters_count = dict()

    for character in text:
        lowerCasedCharacter = character.lower()

        if lowerCasedCharacter in characters_count:
            characters_count[lowerCasedCharacter] += 1
        else:
            characters_count[lowerCasedCharacter] = 1
        

    return characters_count

def get_sorted_words_count(words_count_dict):
    return sorted(words_count_dict.items(), key=lambda item: item[1], reverse=True)
