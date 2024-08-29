from typing import final

from server.common.exceptions import BusinessLogicFailed


@final
class InvalidFolderMetadata(BusinessLogicFailed):
    pass
