list_letters_ru = [
    'а', 'б', 'в', 'г', 'д',
    'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н',
    'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч',
    'ш', 'щ', 'ь', 'ы', 'ъ',
    'э', 'ю', 'я', ' '
]

list_translate_letters_for_ru = [
    'a', 'b', 'v', 'g', 'd',
    'e', 'yo', 'zh', 'z', 'i',
    'y', 'k', 'l', 'm', 'n',
    'o', 'p', 'r', 's', 't',
    'u', 'f', 'kh', 'ts', 'ch',
    'sh', 'sch', '', 'y', '',
    'e', 'yu', 'ya', '-'
]


def translate(word, lang='en'):
    newword = word
    newword_array = []

    for i in range(len(newword)):
        for k in range(len(list_letters_ru)):
            if newword[i] == list_letters_ru[k]:
                newword_array.append(list_translate_letters_for_ru[k])

    assembly_array = ''
    for i in newword_array:
        assembly_array = assembly_array + i

    return assembly_array
