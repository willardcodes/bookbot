def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_text('./books/frankenstein.txt')
    word_count = get_word_count(file_contents)
    character_map = get_char_counts(file_contents)
    characters = chars_counts_to_sorted_list(character_map)
    characters.sort(reverse=True, key=sort_on)
    print(f'--- Begin report of {file_path} ---')
    print(f'{word_count} found in the document\n')
    for c in characters:
        if not c["char"].isalpha():
            continue
        print(f'The \'{c["char"]}\' caracter was found {c["num"]} times')
    print('--- End report ---')

def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_char_counts(file_contents):
    character_map = {}
    for char in file_contents:
        char = char.lower()
        if char in character_map:
            character_map[char] += 1
        else:
            character_map[char] = 1
    return character_map

def chars_counts_to_sorted_list(character_map):
    characters = []
    for char in character_map:
        dict = {"char": char, "num": character_map[char]}
        characters.append(dict)
    return characters

def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    main()
