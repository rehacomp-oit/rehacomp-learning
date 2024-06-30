from typing import Final

from django_test_migrations.migrator import Migrator
from pytest import mark, raises


APPLICATION_NAME: Final = 'learning'


@mark.django_db
def test_0001_vos_organization_model(migrator: Migrator) -> None:
    '''Tests the initial migration forward application.'''

    MODEL_NAME: Final = 'VOSOrganization'

    old_state = migrator.apply_initial_migration((APPLICATION_NAME, None))
    with raises(LookupError):
        old_state.apps.get_model(APPLICATION_NAME, MODEL_NAME)

    new_state = migrator.apply_tested_migration((APPLICATION_NAME, '0001_vos_organization_model'))
    model = new_state.apps.get_model(APPLICATION_NAME, MODEL_NAME)
    assert model.objects.create(organization_name='some organization')


@mark.django_db
def test_0002_course_model(migrator: Migrator) -> None:
    '''
    Tests a migration that creates a table
    for storing information about courses.
    '''

    MODEL_NAME: Final = 'Course'

    old_state = migrator.apply_initial_migration((APPLICATION_NAME, '0001_vos_organization_model',))
    with raises(LookupError):
        old_state.apps.get_model(APPLICATION_NAME, MODEL_NAME)

    new_state = migrator.apply_tested_migration((APPLICATION_NAME, '0002_course_model'))
    model = new_state.apps.get_model(APPLICATION_NAME, MODEL_NAME)
    assert model.objects.create(course_name='s1', course_short_name='s2')
