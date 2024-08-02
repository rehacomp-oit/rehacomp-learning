from dataclasses import dataclass
from datetime import datetime
from typing import final, NewType, Self

from ulid import ULID

from .constants import DATE_FORMAT
from .dto import LearningRequestFrontDTO


LearningRequestId = NewType('LearningRequestId', ULID)


@final
@dataclass(slots=True)
class LearningRequestFront:
    id: LearningRequestId  # noqa: VNE003
    created_at: datetime
    candidate_full_name: str
    course_name: str


    @classmethod
    def from_dto(cls, src: LearningRequestFrontDTO) -> Self:
        learning_request_id = LearningRequestId(src['id'])
        candidate_name = f'{src['candidate__first_name']} {src['candidate__patronymic']} {src['candidate__last_name']}'
        return cls(
            id=learning_request_id,
            created_at=src['created_at'],
            candidate_full_name=candidate_name,
            course_name=src['course__course_name']
        )


    @property
    def string_id(self) -> str:
        return self.id.str


    @property
    def creation_date_string(self) -> str:
        return self.created_at.strftime(DATE_FORMAT)
