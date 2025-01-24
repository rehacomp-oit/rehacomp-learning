from dataclasses import asdict, dataclass
from typing import Any, final, TypedDict


@final
@dataclass(frozen=True, slots=True)
class CourseDTO:
    name: str
    reference: str


@final
@dataclass(frozen=True, slots=True)
class RequestFormOptions:
    course_choices: tuple[tuple[str, str], ...]
    organization_choices: tuple[tuple[str, str], ...]
    disability_group_choices: tuple[tuple[int, str], ...]
    training_level_choices: tuple[tuple[int, str], ...]


    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@final
class LearningRequestFormOutput(TypedDict):
    first_name: str
    patronymic: str
    last_name: str
    birth_year: int
    organization: str
    disability_group: int
    education: str
    job: str
    is_known_braille: bool
    has_device: bool
    training_level: int
    personal_phone: str
    email: str
    course: str
    is_archived: bool
    comments: str
