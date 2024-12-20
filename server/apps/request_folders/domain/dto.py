from dataclasses import asdict, dataclass
from typing import Any, final


@final
@dataclass(frozen=True, slots=True)
class CourseFolder:
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
