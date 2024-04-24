from os.path import join, splitext
from typing import Final

from django.db.models import Model


def build_upload_path(instance: Model, source_filename: str) -> str:
    '''Returns the generated string with path for the uploaded learning request source file.'''

    LEARNING_REQUEST_UPLOAD_DIR: Final = 'learning_requests'

    source_file_suffix = splitext(source_filename)[1]
    new_filename = f'{instance.target_name}{source_file_suffix}'
    return join(LEARNING_REQUEST_UPLOAD_DIR, new_filename)
