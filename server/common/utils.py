from re import sub
from unicodedata import normalize

from ulid import new, ULID


_translate_table = str.maketrans(
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    'abvgdeejzijklmnoprstufhzcss_y_eua'
)


def make_ULID() -> ULID:
    return new()


def slugify_text(source_text: str) -> str:
    '''
    Converts text into a format suitable for url generation.

    convert Cyrillic characters to ascii. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    '''

    tmp_string = source_text.lower().translate(_translate_table)
    tmp_string = normalize('NFKD', tmp_string).encode('ascii', 'ignore').decode('ascii')
    tmp_string = sub(r'[^\w\s-]', '', tmp_string)
    return sub(r'[-\s]+', '-', tmp_string).strip('-_')
