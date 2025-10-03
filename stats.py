def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sorted_list_of_characters(characters_dict):
    list_of_characters = []
    for char in characters_dict:
        list_of_characters.append({"char": char, "num": characters_dict[char]})
    list_of_characters.sort(key=sort_on, reverse=True)
    return list_of_characters

def sort_on(item):
    return item["num"]