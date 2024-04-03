from dataclasses import dataclass
from json import load
from pathlib import Path
from typing import final

from django.db.models import Model


@dataclass(slots=True)
@final
class CreateInitialDataDumpService:
    '''
    Fills the database with prepared data about
    the VOS organization, as well as information
    about available courses.
    '''

    course_model: Model
    vos_organization_model: Model
    input_file_path: Path


    def __call__(self) -> bool:
        with open(self.input_file_path) as file_object:
            source_data = load(file_object)

        batch1 = (
            self.course_model(**course)
            for course in source_data['course']
        )
        batch2 = (
            self.vos_organization_model(**organization)
            for organization in source_data['vos']
        )
        self.course_model.objects.bulk_create(batch1)
        self.vos_organization_model.objects.bulk_create(batch2)
        return True
