from typing import final

from pytest import mark
from returns.result import Failure, Success
from server.apps.core.business_error_types import FolderListFailure
from server.apps.core.services import CourseFoldersListService


@final
class MockCourseRepository:
    def __init__(self, initial_data: tuple[str, ...]) -> None:
        self.__storage = initial_data


    def load_course_full_names(self) -> tuple[str, ...]:
        return self.__storage


@mark.module
@final
class TestCourseFoldersListService:
    def test_success_execution(self) -> None:
        data = ('course1', 'course2', 'course3',)
        get_course_folders = CourseFoldersListService(MockCourseRepository(data))
        expected_value = get_course_folders()
        actual_value = Success(data)
        assert expected_value == actual_value


    def test_failure_execution(self) -> None:
        data = ('',)
        get_course_folders = CourseFoldersListService(MockCourseRepository(data))
        expected_value = get_course_folders()
        actual_value = Failure(FolderListFailure.BROKEN_FOLDER_NAME)
        assert expected_value == actual_value
