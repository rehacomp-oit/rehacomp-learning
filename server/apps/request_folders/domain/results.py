from enum import StrEnum
from typing import final


@final
class GetCourseFoldersFailure(StrEnum):
    MISSING_DATA = 'Сourse folders were not found!'
    CRITICAL_FAILURE = 'Critical error with the data warehouse!'


@final
class GetRequestFormOptionFailure(StrEnum):
    MISSING_DATA = 'The requested data was not found!'
    CRITICAL_FAILURE = 'Critical error with the data warehouse!'
