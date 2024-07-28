from typing import Final, final

from server.utilites.common.types import BaseEnum


LEARNING_REQUEST_STATUS_LENGTH: Final = 10


@final
class LearningRequestStatuses(str, BaseEnum):
    '''
    Available status variants for learning requests.
    '''

    REGISTERED = 'registered'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    IN_ARCHIVE = 'in_archive'
