from typing import NewType

from ulid import ULID


CourseFolderId = NewType('CourseFolderId', ULID)
