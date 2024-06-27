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
