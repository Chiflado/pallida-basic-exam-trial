dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word):
    new_item = {}
    new_item[hun_word] = eng_word
    dictionary.append(dict(new_item))

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    english_dictionary = []
    hungarian_dictionary = []
    for word_to_translate in dictionary:
        for key, value in word_to_translate.items():
            hungarian_dictionary.append(key)
            english_dictionary.append(value)
            if value == eng_word:
                print(key)



def translate_to_eng(hun_word):
    english_dictionary = []
    hungarian_dictionary = []
    for word_to_translate in dictionary:
        for key, value in word_to_translate.items():
            hungarian_dictionary.append(key)
            english_dictionary.append(value)
            if key == hun_word:
                print(value)

add_word('cirtom', 'lemon')
translate_to_hun('lemon')
translate_to_eng('fa')