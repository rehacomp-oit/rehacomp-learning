from typing import final

from server.exceptions import BusinessLogicFailed


@final
class InvalidFolderMetadata(BusinessLogicFailed):
    pass
