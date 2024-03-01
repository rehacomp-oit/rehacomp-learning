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
