from ulid import new, ULID


def make_ULID() -> ULID:
    return new()


def transliterate_text(text: str) -> str:
    '''
    transliterates the letters of the Russian alphabet.
    '''

    source = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    destenation = 'abvgdeejzijklmnoprstufhzcss_y_eua'
    translate_table = str.maketrans(source, destenation)
    return text.lower().translate(translate_table)
