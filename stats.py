def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    dictionary = {}
    for char in text:
        char_lower = char.lower()
        # add the number of times each char appears in text to the dictionary
        if char_lower in dictionary:
            dictionary[char_lower] += 1
        else:
            dictionary[char_lower] = 1
    return dictionary

def sorted_list(dict):
    list_of_dicts = []
    for key, value in dict.items():
        new_dict = {}
        new_dict[key] = value
        list_of_dicts.append(new_dict)
    return sorted(list_of_dicts, reverse=True, key=lambda d: list(d.values())[0])

