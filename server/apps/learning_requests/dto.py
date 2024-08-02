from datetime import datetime
from typing import final, TypedDict

from ulid import ULID


@final
class LearningRequestFrontDTO(TypedDict):
    id: ULID  # noqa: VNE003
    created_at: datetime
    candidate__first_name: str
    candidate__patronymic: str
    candidate__last_name: str
    course__course_name: str
