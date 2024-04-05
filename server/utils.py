from json import load
from pathlib import Path
from typing import Any


def load_from_json_file(file_path: Path) -> Any:
    '''Returns deserialized data from a json file.'''

    with open(file_path) as file_object:
        return load(file_object)
