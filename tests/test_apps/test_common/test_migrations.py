from django_test_migrations.migrator import Migrator
from pytest import raises


def test_0001_vos_organization_model(migrator: Migrator) -> None:
    '''Tests the initial migration forward application.'''

    old_state = migrator.apply_initial_migration(('common', None))
    with raises(LookupError):
        old_state.apps.get_model('common', 'VOSOrganization')

    new_state = migrator.apply_tested_migration(
        ('common', '0001_vos_organization_model')
    )
    model = new_state.apps.get_model('common', 'VOSOrganization')
    assert model.objects.create(organization_name='some organization')


def test_0002_course_model(migrator: Migrator) -> None:
    '''
    Tests a migration that creates a table
    for storing information about courses.
    '''

    old_state = migrator.apply_initial_migration(
        ('common', '0001_vos_organization_model',)
    )
    with raises(LookupError):
        old_state.apps.get_model('common', 'Course')

    new_state = migrator.apply_tested_migration(
        ('common', '0002_course_model')
    )
    model = new_state.apps.get_model('common', 'Course')
    assert model.objects.create(course_name='s1', course_short_name='s2')
