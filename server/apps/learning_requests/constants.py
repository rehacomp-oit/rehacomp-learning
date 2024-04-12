from typing import Final, final

from server.common_tools.types import BaseEnum


LEARNING_REQUEST_FILE_NAME_LENGTH: Final = 20
LEARNING_REQUEST_STATUS_LENGTH: Final = 10


@final
class LearningRequestStatuses(str, BaseEnum):
    '''Available status variants for learning requests'''

    REGISTERED = 'registered'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    IN_HISTORY = 'in_history'
